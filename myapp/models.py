from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.blog_title

class Comment(models.Model):
    comment_text = models.TextField()
    user_rating = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100) 
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment_text
        
  