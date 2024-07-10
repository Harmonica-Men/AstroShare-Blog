from django.urls import path, include
from .views import FrontpageView, HomepageView, ArticleDetailView


urlpatterns = [
    path('', HomepageView, name= 'homepage'),
    path('frontpage/', FrontpageView.as_view(), name= 'frontpage-blogpost'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail')
]
