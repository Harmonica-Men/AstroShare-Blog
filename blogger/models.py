from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime, date
from cloudinary.models import CloudinaryField


class Category(models.Model):
    name = models.CharField(max_length=200)
#     # title = models.CharField(max_length=255)
#     # slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('frontpage-blogpost') 

class Profile(models.Model):
    # 1 to 1 database relation
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_pic = CloudinaryField('image', null = True, blank= True) #up_load to /image/profile
    website_url = models.CharField(max_length=100, null=True, blank=True)
    twitter_url = models.CharField(max_length=100, null=True, blank=True)
    instagram_url = models.CharField(max_length=100, null=True, blank=True)
    facebook_url = models.CharField(max_length=100, null=True, blank=True)
    pinterest = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
       return str(self.user)

    def get_absolute_url(self):
        return reverse('frontpage') 
      

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    CHOICES_STATUS = (
    (ACTIVE, 'Active'),
    (DRAFT, 'Draft')
    )
    
    title = models.CharField(max_length=200)
    image = CloudinaryField('image', null = True, blank= True) # upload_to="images/"
    title_tag = models.CharField(max_length=200, default= "star gazer")
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, default='coding')
    likes = models.ManyToManyField(User, related_name='blog_posts_likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk':self.pk})
        # return reverse('frontpage-blogpost') 
        # return f'/{self.category.slug}/{self.slug}/'

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