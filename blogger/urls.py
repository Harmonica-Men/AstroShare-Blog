from django.urls import path, include
from .views import FrontpageView, HomepageView, ArticleDetailView, AddPostView


urlpatterns = [
    path('add_newpost/', AddPostView.as_view(), name='add-newpost'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('frontpage/', FrontpageView.as_view(), name= 'frontpage-blogpost'),
    path('', HomepageView, name= 'homepage'),
]
