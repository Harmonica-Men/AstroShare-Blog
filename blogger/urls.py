from django.urls import path, include
from .views import FrontpageView, HomepageView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView
from .views import CategoryView, CategoryListView, LikeView, AddCommentView, SearchView, nasa_picture_of_the_day, iss_location
from .views import subscribe, confirm_subscription

urlpatterns = [
    path('', HomepageView, name= 'homepage'),
    path('add_newpost/', AddPostView.as_view(), name='add-newpost'),
    path('add_newcategory/', AddCategoryView.as_view(), name='add-newcategory'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('frontpage/', FrontpageView.as_view(), name= 'frontpage-blogpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name= 'update-post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name= 'delete-post'),
    path('like/<int:pk>', LikeView, name='like-post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name= 'add-comment'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category-list'),
    path('search/', SearchView.as_view(), name='search'),
    path('nasa/', nasa_picture_of_the_day, name='nasa-picture-of-the-day'),
    path('iss_location/', iss_location, name='iss-location'),
    path('subscribe/', subscribe, name='subscribe'),
    path('confirm/', confirm_subscription, name='confirm-subscription'),
]
