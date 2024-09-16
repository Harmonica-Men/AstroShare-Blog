import uuid
import logging
import plotly.graph_objects as go
import plotly.io as pio
import requests

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,
    TemplateView, FormView
)
from django.views import View
from .models import Comment, Profile
from .models import Post, Category, Subscriber
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, SubscriptionForm
from .forms import PostForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from datetime import datetime
from django.http import HttpResponseForbidden
import requests


class ApodView(View):
    """
    View to display NASA's Astronomy Picture of the Day (APOD)
    by fetching data from the NASA API.
    """
    def get(self, request, *args, **kwargs):
        """
        Handles the GET request to fetch APOD
        data and render it on the template.
        """
        api_key = settings.NASA_API_KEY
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
        response = requests.get(url)
        data = response.json()

        # Background image URL
        bg_image_url = 'images/background.webp'

        # Pass the data to the template
        context = {
            'title': data.get('title'),
            'image_url': data.get('url'),
            'explanation': data.get('explanation'),
            'date': data.get('date'),
            'media_type': data.get('media_type'),
            'bg_image_url': bg_image_url,
        }

        return render(request, 'nasa_picture.html', context)


def CategoryView(request, cats):
    """
    View to display posts belonging to a specific category.
    """
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(
        request,
        'categories.html',
        {
            'cats': cats.title().replace('-', ' '),
            'category_posts': category_posts,
        }
    )


def category_list_view(request):
    """
    View to display a list of all categories.
    """
    cat_menu_list = Category.objects.all()
    return render(
        request,
        'category_list.html',
        {
            'cat_menu_list': cat_menu_list
        }
    )


def LikeView(request, pk):
    """
    View to handle liking and unliking a post.
    """
    post = get_object_or_404(Post, pk=pk)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomepageView(TemplateView):
    """
    View to render the homepage of the blog with
    a list of posts and recent profiles.
    """
    model = Post
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        """
        Add the list of posts and recent profiles to the context.
        """
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()

        profiles = (
            Profile.objects.select_related('user')
            .order_by('-user__date_joined')[:9]
        )

        context['profile_names'] = [
            {
                'first_name': profile.user.first_name,
                'last_name': profile.user.last_name,
                'username': profile.user.username,
            }
            for profile in profiles
        ]

        return context


class FrontpageView(ListView):
    """
    View to display a list of recent posts on the front page, with pagination.
    """
    model = Post
    template_name = 'frontpage.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        """
        Add category menu to the context.
        """
        context = super(FrontpageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = Category.objects.all()
        return context


class ArticleDetailView(DetailView):
    """
    View to display the details of a specific post,
    along with like status and total likes.
    """
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        """
        Add like status, total likes, and category menu to the context.
        """
        cat_menu = Category.objects.all()
        context = super(
            ArticleDetailView, self).get_context_data(*args, **kwargs)
        helper = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = helper.total_likes()
        liked = False
        if helper.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    """
    View to add a new blog post.
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('frontpage-blogpost')

    def form_valid(self, form):
        """
        Set the author of the post to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(CreateView):
    """
    View to add a comment to a post.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        """
        Set the post_id of the comment to the current post before saving.
        """
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the post detail page after successfully adding a comment.
        """
        return reverse('article-detail', kwargs={'pk': self.kwargs['pk']})


class UpdatePostView(UpdateView):
    """
    View to update an existing post.
    Only the author of the post is allowed to update it.
    """
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Check if the user is the author of the post.
        If not, return a 403 Forbidden response.
        """
        post = self.get_object()

        if request.user.is_authenticated:
            if request.user == post.author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return render(request, '403.html', status=403)
        else:
            return render(request, '403.html', status=403)

    def get_object(self):
        """
        Fetch the post to be updated.
        """
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)


class DeletePostView(DeleteView):
    """
    View to delete an existing post.
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage-blogpost')


class AddCategoryView(CreateView):
    """
    View to add a new category to the blog.
    """
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


def search_view(request):
    """
    View to search for posts based on a query.
    """
    query = request.GET.get('query', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )
    my_posts = Post.objects.filter(status='draft')

    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'search.html', context)

class NasaPictureOfTheDayView(TemplateView):
    """
    View to fetch and display NASA's Astronomy Picture of the Day (APOD).
    """
    template_name = 'nasa_picture.html'

    def get_context_data(self, **kwargs):
        # Fetch the base context from the parent class
        context = super().get_context_data(**kwargs)
        
        # NASA_API_KEY is available in the settings
        
        nasa_api_key = getattr(settings, 'NASA_API_KEY', None)
        url = f"https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}"
        
        # Initialize data with default values
        data = {}
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            context['error'] = f"Error fetching APOD: {str(e)}"
        
        # Add NASA APOD data to context
        context['title'] = data.get('title', 'No title available')
        context['image_url'] = data.get('url', '')
        context['media_type'] = data.get('media_type', 'image')
        context['explanation'] = data.get('explanation', 'No explanation available')
        context['date'] = data.get('date', 'No date available')
        context['bg_image_url'] = 'images/background.webp'
        
        return context


def iss_location(request):
    """
    View to fetch and display the current location of
    the International Space Station (ISS) on a map.
    """
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    fig = go.Figure()
    fig.add_trace(go.Scattergeo(
        lon=[longitude],
        lat=[latitude],
        text="Current ISS Location",
        mode='markers',
        marker=dict(size=12, color='red')
    ))

    fig.update_layout(
        geo_scope='world',
    )

    fig_html = pio.to_html(fig, full_html=False)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    return render(request, 'iss_location.html', {
        'plot_html': fig_html,
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    })


logger = logging.getLogger(__name__)


class SubscribeView(FormView):
    """
    View to handle user subscriptions to the blog via email.
    """
    form_class = SubscriptionForm
    template_name = 'homepage.html'

    def form_valid(self, form):
        """
        Process the subscription form and send a confirmation email.
        """
        login = form.cleaned_data['login']
        email = form.cleaned_data['email']
        confirmation_code = str(uuid.uuid4())
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        subscriber.confirmation_code = confirmation_code
        subscriber.is_confirmed = False
        subscriber.save()
        confirmation_link = (
            f"{self.request.scheme}://{self.request.get_host()}"
            f"/blogger/confirm/?code={confirmation_code}"
        )
        subject = 'Confirm your subscription'
        message = (
            f"Hello {login},\n\n"
            f"Click the link to confirm your subscription: {confirmation_link}"
        )
        from_email = settings.DEFAULT_FROM_EMAIL
        try:
            send_mail(subject, message, from_email, [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            logger.error(f'Error sending email: {e}')
            return HttpResponse(f'Error sending email: {e}')

        return HttpResponseRedirect(reverse_lazy('check-email'))


class CheckEmailView(TemplateView):
    """
    View to display a page asking the user to check their email,
    for a subscription confirmation link.
    """
    template_name = 'registration/check_email.html'


def confirm_subscription(request):
    """
    View to confirm the user's subscription
    using the provided confirmation code.
    """
    code = request.GET.get('code')

    if not code:
        return HttpResponse('Confirmation code is required.', status=400)

    subscriber = get_object_or_404(Subscriber, confirmation_code=code)
    subscriber.is_confirmed = True
    subscriber.save()

    return render(request, 'registration/confirm_subscription.html')
