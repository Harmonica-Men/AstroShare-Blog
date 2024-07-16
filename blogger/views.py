from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Category
from django.urls import reverse_lazy, reverse
from .forms import PostForm


# from django.utils.text import slugify

def HomepageView(request): # Homepage view
    return render(request, 'homepage.html')

class FrontpageView(ListView): # Frontpage view for the Blog Post
    model = Post
    template_name = 'frontpage.html'
    cats = Category.objects.all()
    ordering = ['-post_date'] #show post on publication date reverse

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(FrontpageView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# function 
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
 

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts': category_posts})
 
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post   
    form_class = PostForm
    template_name = 'update_post.html'
#    fields = ('title', 'title_tag', 'body')

class DeletePostView(DeleteView):
    model = Post   
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage-blogpost')

# def register(request):
#     return render(request, 'register.html')

class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'


