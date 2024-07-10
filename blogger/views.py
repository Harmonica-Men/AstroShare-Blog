from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post

# def homepage(request): # Homepage view
#     return render(request, 'homepage.html')

class FrontpageView(ListView): # Frontpage view for the Blog Post
    model = Post
    template_name = 'frontpage.html'

