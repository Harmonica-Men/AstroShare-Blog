from django.urls import path
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView, ShowProfilePageView, EditProfilePageView
#from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('<int:pk>/password/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    ]