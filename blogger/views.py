from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

def HomepageView(request): # Homepage view
    return render(request, 'homepage.html')

class FrontpageView(ListView): # Frontpage view for the Blog Post
    model = Post
    template_name = 'frontpage.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
