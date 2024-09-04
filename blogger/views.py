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
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, pk=pk)
    liked = post.likes.filter(id=request.user.id).exists()
    if liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomepageView(TemplateView):
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
    model = Post
    template_name = 'frontpage.html'
    context
