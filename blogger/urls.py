from django.urls import path, include
from .views import FrontpageView, HomepageView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView
#from .views import FrontpageView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomepageView, name= 'homepage'),
    path('add_newpost/', AddPostView.as_view(), name='add-newpost'),
    path('add_newcategory/', AddCategoryView.as_view(), name='add-newcategory'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('frontpage/', FrontpageView.as_view(), name= 'frontpage-blogpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name= 'delete-post'),
    path('category/<str:cats>/', CategoryView.as_view(), name='category'),
]
