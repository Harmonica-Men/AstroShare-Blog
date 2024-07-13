from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm


class UserRegisterView(generic.CreateView):
    #form_class = UserCreationForm
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    #form_class = UserCreationForm
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('frontpage')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_succes')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('frontpage')  # Redirect to frontpage after password change

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_object()
        return kwargs