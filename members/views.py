from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blogger.models import Profile

class CreateProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def get_object(self, queryset=None):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('frontpage-blogpost')

    def get_object(self, queryset=None):
        return self.request.user.profile
    

class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context 

class AuthorProfileView(DetailView):
    model = Profile
    template_name = 'registration/author_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        return get_object_or_404(Profile, user__id=self.kwargs['id'])           

class UserRegisterView(generic.CreateView):
    # form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    # form_class = UserCreationForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('frontpage-blogpost')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_succes')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('frontpage-blogpost')  # Redirect to frontpage after password change

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_object()
        return kwargs