from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from markdown import markdown
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_pic')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Post(models.Model):
    content = models.TextField()
    description = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts_pic')
    category = models.ForeignKey(Category, related_name='posts_category', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='user_posts', on_delete =models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name='likes')
    users_who_fav = models.ManyToManyField(User, related_name='faves')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    def like_count(self):
        return self.users_who_like.all().count()
    


class Comment(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, related_name='comments', on_delete =models.CASCADE)
    post_in = models.ForeignKey(Post, related_name='comments', on_delete =models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
  
    

    
    

    
    
    
