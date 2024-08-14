from django import forms
from .models import Comment, Subscriber
from .models import Post, Category

# from .models import Post, Category

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")

    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

choices = Category.objects.all().values_list('name', 'name')



# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'title_tag', 'author', 'category', 'body', 'image']
#         widgets = {
#             'author': forms.HiddenInput(),
#         }

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('title', css_class='form-control', placeholder='title of the post', label='Title', wrapper_class='mb-3', style='padding: 20px;'),)

        

    # category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'title_tag', 'author', 'category', 'body', 'image']

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
        
#         self.helper.layout = Layout(
#             'title_tag',
#             'author',
#             Row(
#                 Column('category', css_class='form-group col-md-6 mb-0'),
#                 Column('body', css_class='form-group col-md-6 mb-0'),
#                 css_class='form-row'
#             ),
#             'image',
#             Submit('submit', 'Post')
#         )
#         # self.fields('title', css_class='form-control', placeholder='title of the post', label='Title', wrapper_class='mb-3', style='padding: 20px;',)
        
#         self.fields['category'].initial = 'Solar Storms'

#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")

# class PostForm(forms.ModelForm):
#     class Meta: 
#         model = Post
#         fields = ('title', 'title_tag', 'author', 'category', 'body', 'image')

#         widgets = {
#             'title' : forms.TextInput(attrs={'class': 'form-control'}),
#             'title_tag' : forms.TextInput(attrs={'class': 'form-control'}),

#             'author' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user name', 'id': 'js_id', 'type': 'hidden'}),

#             'author': forms.HiddenInput(),


#             'category' : forms.Select(choices=choices, attrs={'class': 'form-control','placeholder': 'choice'}),
#             'body' : forms.Textarea(attrs={'class': 'form-control'}),            
#         }

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'title_tag', 'author', 'category', 'body', 'image']
       

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field('title', css_class='form-control', placeholder='title of the post', label='Title', wrapper_class='mb-3', style='padding: 20px;'),
#             # Field('content', css_class='form-control', placeholder='Content of the post', wrapper_class='mb-3', style='padding: 20px;'),
#             # Field('image', css_class='form-control', wrapper_class='mb-3', style='padding: 20px;'),
#             Submit('submit', 'Post', css_class='btn btn-secondary')
#         )
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Submit'))

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
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    