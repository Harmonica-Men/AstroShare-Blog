from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View
from .models import Post, Category, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm, CommentForm
from django.db.models import Q

import plotly.graph_objects as go
import plotly.io as pio

import requests


# from django.utils.text import slugify



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


    # post.likes.add(request.user)
    # return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

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

class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        query = request.GET.get('query', '')
        posts = Post.objects.filter(status=Post.ACTIVE).filter(
            Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query)
        )
        context = {
            'posts': posts,
            'query': query,
        }
        return render(request, self.template_name, context)

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
    # Fetch ISS location data
    response = requests.get('http://api.open-notify.org/iss-now.json')
    data = response.json()
    latitude = float(data['iss_position']['latitude'])
    longitude = float(data['iss_position']['longitude'])

    # Create Plotly figure
    fig = go.Figure(go.Scattergeo(
        lon=[longitude],
        lat=[latitude],
        text="ISS",
        mode='markers',
        marker=dict(size=10, color='red')
    ))

    fig.update_layout(
        title='Current Location of the ISS',
        geo_scope='world',
    )

    # Convert the figure to HTML
    fig_html = pio.to_html(fig, full_html=False)

    # Render the template with the plot and ISS coordinates
    return render(request, 'iss_location.html', {
        'plot_html': fig_html,
        'latitude': latitude,
        'longitude': longitude
    })
