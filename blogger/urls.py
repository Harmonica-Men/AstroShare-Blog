from django.urls import path
from .views import (
    AddCategoryView, AddCommentView, AddPostView, ApodView, ArticleDetailView,
    category_list_view, CategoryView, CheckEmailView, confirm_subscription,
    DeletePostView, FrontpageView, HomepageView, iss_location, LikeView,
    search_view, SubscribeView, UpdatePostView
)

urlpatterns = [
    # Homepage view
    path('', HomepageView.as_view(), name='homepage'),
    # Add a new post
    path('add_newpost/', AddPostView.as_view(), name='add-newpost'),
    # Add a new category
    path(
        'add_newcategory/', AddCategoryView.as_view(), name='add-newcategory'
    ),
    # Detail view of a specific article identified by primary key (pk)
    path(
        'article/<int:pk>/', ArticleDetailView.as_view(),
        name='article-detail'
    ),
    # Frontpage view for blog posts
    path('frontpage/', FrontpageView.as_view(), name='frontpage-blogpost'),
    # date a specific article identified by primary key (pk)
    path(
        'article/edit/<int:pk>/', UpdatePostView.as_view(), name='update-post'
    ),
    # Delete a specific article identified by primary key (pk)
    path(
        'article/<int:pk>/delete/', DeletePostView.as_view(),
        name='delete-post'
    ),
    # Like a specific post identified by primary key (pk)
    path('like/<int:pk>/', LikeView, name='like-post'),
    # Add a comment to a specific article identified by primary key (pk)
    path(
        'article/<int:pk>/comment/', AddCommentView.as_view(),
        name='add-comment'
    ),
    # View articles by category, with category specified by a string parameter
    path('category/<str:cats>/', CategoryView, name='category'),
    # List all categories
    path('category_list/', category_list_view, name='category-list'),
    # Search view
    path('search/', search_view, name='search'),
    # NASA picture of the day
    path('nasa/', ApodView.as_view(), name='nasa-picture-of-the-day'),
    # View ISS location
    path('iss_location/', iss_location, name='iss-location'),
    # Subscribe to a newsletter or service
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    # Check email view
    path('check-email/', CheckEmailView.as_view(), name='check-email'),
    # Confirm subscription
    path('confirm/', confirm_subscription, name='confirm-subscription'),
]
