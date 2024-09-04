from django import forms
from .models import Post, Category, Comment

# Form for creating or editing blog posts
class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),  # All categories
        empty_label="Select Category"  # Placeholder text
    )

    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post message text here...'
            }),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

# Choices for categories
choices = Category.objects.all().values_list('name', 'name')

# Form for submitting comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your name'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'write your comment'
            }),
        }

# Form for user subscriptions
class SubscriptionForm(forms.Form):
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
