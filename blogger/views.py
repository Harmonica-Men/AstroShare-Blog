from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Category
from .forms import PostForm

def HomepageView(request): # Homepage view
    return render(request, 'homepage.html')

class FrontpageView(ListView): # Frontpage view for the Blog Post
    model = Post
    template_name = 'frontpage.html'
    ordering = ['-id'] #reverse order post
 
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

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

# function 
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class CategoryView(View):
    template_name = 'categories.html'
    error_template_name = '404.html'

    def get(self, request, cats):
        try:
            category = get_object_or_404(Category, name=cats)
            category_posts = Post.objects.filter(category=category)
            context = {
                'cats': category.name,
                'category_posts': category_posts,
            }
            return render(request, self.template_name, context)
        except Http404:
            return render(request, self.error_template_name, status=404)