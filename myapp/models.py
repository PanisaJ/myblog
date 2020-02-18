from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.blog_title
    
    @property
    def sorted_comment_set(self):
        return self.comment_set.order_by('-created_on')

class Comment(models.Model):
    comment_text = models.TextField()
    user_rating = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text
        
  