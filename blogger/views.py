import uuid
import logging
import plotly.graph_objects as go
import plotly.io as pio
import requests

from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
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
from django.utils.text import slugify

from django.shortcuts import render

def apod_view(request):
    bg_image_url = 'images/background.webp'
    # Include other context data as needed
    context = {
        'bg_image_url': bg_image_url,
        'title': 'Your Title',
        'media_type': 'image',  # or 'video'
        'image_url': 'path/to/your/image_or_video',
        'date': '2024-09-01',
        'explanation': 'Your explanation here...',
    }
    return render(request, 'apod.html', context)


from django.conf import settings
from django.shortcuts import render
from django.views import View
import requests

class ApodView(View):
    def get(self, request, *args, **kwargs):
        # NASA API URL with your API key
        url = f"https://api.nasa.gov/planetary/apod?api_key={settings.NASA_API_KEY}"
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
            'media_type': data.get('media_type'),  # For checking if it's a video or image
            'bg_image_url': bg_image_url,  # Add background image URL
        }

        return render(request, 'nasa_picture.html', context)


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
 
def LikeView(request, pk):
    # post = get_object_or_404(Post, id=request.POST.get('post_id'))
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
    model = Post
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()

        # Fetch the latest 9 profiles with user details
        profiles = Profile.objects.select_related('user').order_by('-user__date_joined')[:9]

        # Extracting first name, last name, and username into a list of dictionaries
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
    model = Post
    template_name = 'frontpage.html'  # Ensure this is the correct template for the front page
    context_object_name = 'posts'
    ordering = ['-post_date']
    paginate_by = 5  # Display 5 posts per page

    def get_context_data(self, *args, **kwargs):
        context = super(FrontpageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = Category.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
       cat_menu = Category.objects.all()
       context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

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
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('frontpage-blogpost')  

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the current user
        return super().form_valid(form)

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('frontpage-blogpost')  # Change to your desired success URL

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()

        if request.user.is_authenticated:
            if request.user == post.author:
                return super().dispatch(request, *args, **kwargs)
            else:
                return render(request, '403.html', status=403)
        else:
            return render(request, '403.html', status=403)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post, pk=pk)

class DeletePostView(DeleteView):
    model = Post   
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage-blogpost')

class AddCategoryView(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

def search_view(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(status=Post.ACTIVE).filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    )
    context = {
        'posts': posts,
        'query': query,
    }
    return render(request, 'search.html', context)
   
def nasa_picture_of_the_day(request):
    api_key = 'ZXlNkoGPeg9qsaroBYKtRv8SlyR0jnjNIY0QzBrh'  # Replace with your NASA API key
    url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'
    response = requests.get(url)
    data = response.json()
    
    context = {
        'title': data.get('title'),
        'image_url': data.get('url'),
        'explanation': data.get('explanation'),
    }
    
    return render(request, 'nasa_picture.html', context)


def iss_location(request):
    # Fetch current ISS location data
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    # Create Plotly figure for the ISS current location only
    fig = go.Figure()

    # Plot the ISS current location
    fig.add_trace(go.Scattergeo(
        lon=[longitude],
        lat=[latitude],
        text="Current ISS Location",
        mode='markers',
        marker=dict(size=12, color='red')  # Increased marker size for visibility
    ))

    fig.update_layout(
        # title='Current Location of the ISS',
        geo_scope='world',
    )

    # Convert the figure to HTML
    fig_html = pio.to_html(fig, full_html=False)

    # Get the current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Render the template with the plot, ISS coordinates, and timestamp
    return render(request, 'iss_location.html', {
        'plot_html': fig_html,
        'latitude': latitude,
        'longitude': longitude,
        'timestamp': timestamp
    })

logger = logging.getLogger(__name__)

class SubscribeView(FormView):
    form_class = SubscriptionForm
    template_name = 'homepage.html'  # The form will be displayed on the homepage

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
    template_name = 'registration/check_email.html'


def ConfirmSubscription(request):
    code = request.GET.get('code')

    if not code:
        return HttpResponse('Confirmation code is required.', status=400)

    subscriber = get_object_or_404(Subscriber, confirmation_code=code)
    subscriber.is_confirmed = True
    subscriber.save()

    return render(request, 'registration/confirm_subscription.html')
