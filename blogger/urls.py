from django.urls import path, include
from .views import FrontpageView, HomepageView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView
from .views import HomepageView
from .views import LikeView, AddCommentView, SearchView, nasa_picture_of_the_day, iss_location
from .views import SubscribeView, ConfirmSubscription 
from .views import AddCategoryView, CategoryView, CategoryListView, CheckEmailView

urlpatterns = [
    path('', HomepageView.as_view(), name= 'homepage'),
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
    path('subscribe/', SubscribeView.as_view(), name='Subscribe'),
    path('check-email/', CheckEmailView.as_view(), name='check_email'),
    path('confirm/', ConfirmSubscription, name='ConfirmSubscription'),
]
