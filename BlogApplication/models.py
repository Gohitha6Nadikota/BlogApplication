from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    postDate=models.DateField(auto_now_add=True)
    body=RichTextField(blank=True,null=True)
    category=models.CharField(max_length=255,default="uncategorized")
    snippet=models.CharField(max_length=255)
    likes=models.ManyToManyField(User,related_name="blog_posts")

    def __str__(self):
        return self.title + ' | '+ str(self.author)
    
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')
