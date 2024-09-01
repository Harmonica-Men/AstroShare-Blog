from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.db.models.signals import post_save

# from ckeditor.fields import RichTextField
# from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
 
    name = models.CharField(max_length=254, primary_key=True)
    # slug = models.SlugField(unique=True)
    category_discription = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)        
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
        # return self.category_discription

    def get_absolute_url(self):
        return reverse('frontpage-blogpost') 

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image', null = True, blank= True)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
       return str(self.user)

    def get_absolute_url(self):
        return reverse('frontpage-blogpost') 

# class Post begins

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft')
    )
    
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', null = True, blank= True)
    # title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    # slug = models.SlugField()
    # intro = models.TextField()
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    category = models.CharField(max_length=254, default='UAP')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='name')

    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def total_likes(self):
        return self.likes.count()

    
    class Meta:
        ordering = ('-created_at','post_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('frontpage-blogpost') 
        # return f'/{self.category.slug}/{self.slug}/'

# class Post ends


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.TimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.post
       #return '%s - %s' % str(self.post.title, self.name)
    def __str__(self):
        return f'{self.name} - {self.body[:20]}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=50)

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """
    Automatically create a user profile when a new user is created
    """
    if created:
        Profile.objects.create(user=instance)