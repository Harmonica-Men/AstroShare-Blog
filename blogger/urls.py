from django.urls import path, include
from .views import (
    AddCategoryView, AddCommentView, AddPostView, ApodView, ArticleDetailView,
    CategoryListView, CategoryView, CheckEmailView, ConfirmSubscription,
    DeletePostView, FrontpageView, HomepageView, iss_location, LikeView,
    SearchView, SubscribeView, UpdatePostView)

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('add_newpost/', AddPostView.as_view(), name='add-newpost'),
    path(
        'add_newcategory/', AddCategoryView.as_view(), name='add-newcategory'
    ),
    path(
        'article/<int:pk>/', ArticleDetailView.as_view(),
        name='article-detail'
    ),
    path('frontpage/', FrontpageView.as_view(), name='frontpage-blogpost'),
    path(
        'article/edit/<int:pk>/', UpdatePostView.as_view(), name='update-post'
    ),
    path(
        'article/<int:pk>/delete/', DeletePostView.as_view(),
        name='delete-post'
    ),
    path('like/<int:pk>/', LikeView, name='like-post'),
    path(
        'article/<int:pk>/comment/', AddCommentView.as_view(),
        name='add-comment'
    ),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category_list/', CategoryListView, name='category-list'),
    path('search/', search_view, name='search'),
    path('nasa/', ApodView.as_view(), name='nasa-picture-of-the-day'),
    path('iss_location/', iss_location, name='iss-location'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('check-email/', CheckEmailView.as_view(), name='check-email'),
    path('confirm/', ConfirmSubscription, name='confirm-subscription'),
]
