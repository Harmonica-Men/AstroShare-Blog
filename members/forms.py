from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, PasswordChangeForm
)
from django.contrib.auth.models import User
from django import forms
from blogger.models import Profile


class ProfilePageForm(forms.ModelForm):
    """
    Form for updating user profile page information.
    """
    class Meta:
        model = Profile  # Associate form with Profile model
        fields = (
            'bio', 'profile_pic', 'website_url', 'twitter_url',
            'instagram_url', 'facebook_url'
        )
        # Customize widget attributes for the fields
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
            'website_url': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'twitter_url': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'instagram_url': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'facebook_url': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
        }


class SignUpForm(UserCreationForm):
    """
    Form for user signup.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'my@somedomain.org'}
        )
    )
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Associate form with User model
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """
    Form for editing user profile information.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'my@somedomain.org'}
        )
    )
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_login = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Associate form with User model
        fields = ('username', 'first_name', 'last_name', 'email', 'last_login')


class PasswordChangingForm(PasswordChangeForm):
    """
    Form for changing user password.
    """
    old_password = forms.CharField(
        max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User  # Associate form with User model
        fields = ('old_password', 'new_password1', 'new_password1')
