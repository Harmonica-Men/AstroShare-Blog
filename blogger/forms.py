from django import forms
from .models import Post, Category


# Hardcode the list
# choices = [('coding', 'coding'), ('sports', 'sports'), ('voetbal', 'voetbal')]
choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']
# widgits are magic
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            #'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name'}),
            #'category' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.Select(choices=choices, attrs={'class': 'form-control','placeholder': 'choice'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),            
        }


