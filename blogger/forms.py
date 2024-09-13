from django import forms
from .models import Post, Category, Comment


class PostForm(forms.ModelForm):
    """
    A form for creating and updating a blog post.
    """
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category"
    )

    class Meta:
        """
        Meta class to define model and form field settings.
        Fields are selected from the Post model.
        Widgets are defined to style the form fields.
        """
        model = Post
        fields = ['title', 'category', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter post message text here...'
                }
            ),
            'image': forms.FileInput(attrs={'class': 'form-control'}), }
    choices = Category.objects.all().values_list('name', 'name')


class CommentForm(forms.ModelForm):
    """
    A form for adding comments to a blog post.
    """
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your name'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'write your comment'}),
        }


class SubscriptionForm(forms.Form):
    """
    A simple subscription form that collects a user's login and email.
    """
    login = forms.CharField(
        max_length=100,
        label='Login',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'your name'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com',
            'required': True
        })
    )
