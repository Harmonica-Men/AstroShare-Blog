from django import forms
from .models import Post

class PostForm(format.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')
# widgits are magic
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'placeholder test'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),            
        }