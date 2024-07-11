from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

def HomepageView(request): # Homepage view
    return render(request, 'homepage.html')

class FrontpageView(ListView): # Frontpage view for the Blog Post
    model = Post
    template_name = 'frontpage.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__' # because I am lazy
    success_url = reverse_lazy('frontpage-blogpost')  # go back to frontpage of blogpost
