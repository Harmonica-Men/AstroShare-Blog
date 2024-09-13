from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from blogger.models import Profile
from django.urls import reverse

class CreateProfilePageView(generic.UpdateView):
    """
    View for creating and updating the user's profile page.
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def get_object(self, queryset=None):
        """
        Returns the user's profile object, creating one if it doesn't already exist.
        """
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        """
        Automatically associates the user with the profile being created or updated.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    """
    View for editing the user's profile page.
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/edit_profile_page.html'

    def get_object(self, queryset=None):
        """
        Returns the user's profile object for editing.
        """
        return self.request.user.profile

    def get_success_url(self):
        """
        Redirects the user to their profile page after a successful edit.
        """
        # Use the user's profile ID to dynamically build the URL
        return reverse('show-profile-page', kwargs={'pk': self.request.user.profile.id})


class ShowProfilePageView(DetailView):
    """
    View for displaying a user's profile page.
    """
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        """
        Adds the page user to the context, allowing profile details to be displayed.
        """
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context 

class AuthorProfileView(DetailView):
    """
    View for displaying an author's profile.
    """
    model = Profile
    template_name = 'registration/author_profile.html'
    context_object_name = 'profile'

    def get_object(self):
        """
        Fetches the profile of the author using their user ID.
        """
        return get_object_or_404(Profile, user__id=self.kwargs['id'])           

class UserRegisterView(generic.CreateView):
    """
    View for user registration.
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """
    View for editing the logged-in user's profile.
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('frontpage-blogpost')

    def get_object(self):
        """
        Returns the logged-in user object to be edited.
        """
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    """
    View for changing the user's password.
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_succes')

class CustomPasswordChangeView(PasswordChangeView):
    """
    Custom view for changing a user's password with a different success redirect.
    """
    template_name = 'registration/change_password.html'
    success_url = reverse_lazy('frontpage-blogpost')  # Redirect to frontpage after password change

    def get_object(self, queryset=None):
        """
        Fetches the User object using the primary key from the URL.
        """
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        """
        Passes the user object to the password change form.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_object()
        return kwargs