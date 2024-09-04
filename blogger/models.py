from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from cloudinary.models import CloudinaryField
from django.utils.crypto import get_random_string
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
    # Represents a category for blog posts
    name = models.CharField(max_length=254, primary_key=True)
    category_discription = models.TextField(blank=True, null=True)

    class Meta:
        # Orders categories by name in ascending order
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # URL to view the category; adjust the named URL if necessary
        return reverse('frontpage-blogpost')


class Profile(models.Model):
    # Extends the User model to include additional profile information
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image', null=True, blank=True)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        # Returns the username associated with this profile
        return str(self.user)

    def get_absolute_url(self):
        # URL to view the profile; adjust the named URL if necessary
        return reverse('frontpage-blogpost')


class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
        ('archived', 'Archived'),
    ]
    # Represents a blog post
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', null=True, blank=True)
    author = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=254, default='UAP')
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=DRAFT)

    def total_likes(self):
        # Returns the total number of likes for this post
        return self.likes.count()

    class Meta:
        # Reverse order posting
        ordering = ('-created_at', 'post_date',)

    def __str__(self):
        # Returns the title of the post
        return self.title

    def get_absolute_url(self):
        # URL to view the post; adjust the named URL if necessary
        return reverse('frontpage-blogpost')


class Comment(models.Model):
    # Represents a comment on a blog post
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        # Returns the name and the first 20 characters of the comment body
        return f'{self.name} - {self.body[:20]}'


class Subscriber(models.Model):
    # Represents a subscriber to the blog
    email = models.EmailField(unique=True)
    is_confirmed = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=50)

    def __str__(self):
        # Returns the email of the subscriber
        return self.email


# Automatically create a user profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        # Creates a Profile object when a User object is created
        Profile.objects.create(user=instance)
