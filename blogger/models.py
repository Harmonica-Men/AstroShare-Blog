from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    title_tag = models.CharField(max_length=200, default= "star gazer")
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk':self.pk})
        # return reverse('frontpage-blogpost') 
        # return f'/{self.category.slug}/{self.slug}/'