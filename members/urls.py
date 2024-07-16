from django.urls import path
from .views import UserRegisterView, UserEditView, CustomPasswordChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit-profile'),
    path('<int:pk>/password/', CustomPasswordChangeView.as_view(), name='password-change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile-page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit-profile-page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create-profile-page'),
    
    ]