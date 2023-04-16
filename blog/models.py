from datetime import *
from django.utils import timezone
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    slug = models.SlugField(null=False, unique=True, max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

def approve(self):
    self.approved_comment = True
    self.save()

def __str__(self):
    return self.text