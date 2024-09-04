import uuid
import logging
import plotly.graph_objects as go
import plotly.io as pio
import requests

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.views import View
from .models import Comment, Profile, Post, Category, Subscriber
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, SubscriptionForm, PostForm, CategoryForm
from django.db.models import Q
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from datetime import datetime

logger = logging.getLogger(__name__)

def apod_view(request):
    """Render a static page for APOD with predefined context."""
    bg_image_url = 'images/background.webp'
    context = {
        'bg_image_url': bg_image_url,
        'title': 'Your Title',
        'media_type': 'image',
        'image_url': 'path/to/your/image_or_video',
        'date': '2024-09-01',
        'explanation': 'Your explanation here...',
    }
    return render(request, 'apod.html', context)

class ApodView(View):
    """View for fetching and displaying NASA's Astronomy Picture of the Day."""
    def get(self, request, *args, **kwargs):
        url = f"https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}"
        response = requests.get(url)
        if response.status_code != 200:
            return HttpResponse('Error fetching data from NASA API', status=500)
        
        data = response.json()
        bg_image_url = 'images/background.webp'
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
    """Render posts filtered by category."""
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    """Render a list of all categories."""
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def LikeView(request, pk):
    """Toggle like status for a post."""
    post = get_object_or_404(Post, pk=pk)
    liked = post.likes.filter(id=request.user.id).exists()
    if liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomepageView(TemplateView):
    """Display the homepage with recent posts and user profiles."""
    model = Post
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        profiles = Profile.objects.select_related('user').order_by('-user__date_joined')[:9]
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
    """Display a paginated list of posts on the front page."""
    model = Post
    template_name = 'frontpage.html'
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["cat_menu"] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    """Display details of a single post."""
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        helper = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = helper.total_likes()
        liked = helper.likes.filter(id=self.request.user.id).exists()
        context["cat_menu"] = Category.objects.all()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    """Form for adding a new post."""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('frontpage-blogpost')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AddCommentView(CreateView):
    """Form for adding a new comment to a post."""
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.kwargs['pk']})

class UpdatePostView(UpdateView):
    """Form for updating an existing post."""
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if request.user.is_authenticated and request.user == post.author:
            return super().dispatch(request, *args, **kwargs)
        else:
            return render(request, '403.html', status=403)

class DeletePostView(DeleteView):
    """View for deleting a post."""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage-blogpost')

class AddCategoryView(CreateView):
    """Form for adding a new category."""
    model = Category
    form_class = CategoryForm
    template_name = 'add_category.html'

def search_view(request):
    """Search for posts by title or body."""
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )
    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'search.html', context)

def iss_location(request):
    """Fetch and display the current location of the ISS."""
    response = requests.get('http://api.open-notify.org/iss-now.json')
    if response.status_code != 200:
        return HttpResponse('Error fetching ISS location data', status=500)
    
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

class SubscribeView(FormView):
    """Form for subscribing and sending confirmation email."""
    form_class = SubscriptionForm
    template_name = 'homepage.html'

    def form_valid(self, form):
        login = form.cleaned_data['login']
        email = form.cleaned_data['email']
        
        confirmation_code = str(uuid.uuid4())
        subscriber, created = Subscriber.objects.get_or_create(email=email)
        subscriber.confirmation_code = confirmation_code
        subscriber.is_confirmed = False
        subscriber.save()

        confirmation_link = f"{self.request.scheme}://{self.request.get_host()}/blogger/confirm/?code={confirmation_code}"
        subject = 'Confirm your subscription'
        message = f'Hello {login},\n\nClick the link to confirm your subscription: {confirmation_link}'
        from_email = settings.DEFAULT_FROM_EMAIL
        
        try:
            send_mail(subject, message, from_email, [email])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        except Exception as e:
            logger.error(f'Error sending email: {e}')
            return HttpResponse(f'Error sending email: {e}')

        return HttpResponseRedirect(reverse_lazy('check_email'))

class CheckEmailView(TemplateView):
    """Page for informing users to check their email."""
    template_name = 'registration/check_email.html'

def ConfirmSubscription(request):
    """Confirm subscription based on the provided code."""
    code = request.GET.get('code')

    if not code:
        return HttpResponse('Confirmation code is required.', status=400)

    subscriber = get_object_or_404(Subscriber, confirmation_code=code)
    subscriber.is_confirmed = True
    subscriber.save()

    return render(request, 'registration/confirm_subscription.html')
