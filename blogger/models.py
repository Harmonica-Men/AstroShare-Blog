from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save


# Category model with name and description
class Category(models.Model):
    name = models.CharField(max_length=254, primary_key=True)
    category_description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('name',)  # Order categories by name
        verbose_name_plural = 'Categories'  # Plural name for admin

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontpage-blogpost')  # URL for category page


# User profile model with additional fields
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image', null=True, blank=True)
    website_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('frontpage-blogpost')  # URL for profile page


# Post model with status and category
class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )

    title = models.CharField(max_length=200)  # Post title
    image = CloudinaryField('image', null=True, blank=True)
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=CHOICES_STATUS,
        default=ACTIVE)
    category = models.CharField(max_length=254, default='UAP')
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def total_likes(self):
        return self.likes.count()  # Count of likes

    class Meta:
        ordering = ('-created_at', 'post_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('frontpage-blogpost')  # URL for post page


# Comment model associated with posts
class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Commenter's name
    body = models.TextField()  # Comment content
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        # Display first 20 characters of the comment
        return f'{self.name} - {self.body[:20]}'


# Subscriber model for email subscriptions
class Subscriber(models.Model):
    email = models.EmailField(unique=True)  # Unique email address
    is_confirmed = models.BooleanField(default=False)  # Confirmation status
    confirmation_code = models.CharField(max_length=50)  # Email confirmation

    def __str__(self):
        return self.email


# Signal to create a user profile when a new user is created
@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
