from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
 
    name = models.CharField(max_length=254, primary_key=True)
    category_discription = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)        
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

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
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', null = True, blank= True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=254, default='UAP')
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def total_likes(self):
        return self.likes.count()
    
    class Meta:
        ordering = ('-created_at','post_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('frontpage-blogpost') 
        

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.body[:20]}'

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=50)

    def __str__(self):
        return self.email

# Automatically create a user profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)