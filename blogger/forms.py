from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Post, Category, Comment

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")
    body = forms.CharField(widget=SummernoteWidget())  # Using SummernoteWidget for the body field

    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'category', 'body', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

choices = Category.objects.all().values_list('name', 'name')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        # fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'enter your name'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'write your comment'}),
        }

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


    