from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'title_tag', 'author', 'body']
# widgits are magic
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            #'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),            
        }