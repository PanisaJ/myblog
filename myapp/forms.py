from django import forms
from .models import Blog, Comment
from django.shortcuts import get_object_or_404

class BlogForm(forms.Form):
    blog_title = forms.CharField()
    blog_text = forms.CharField(widget=forms.Textarea())
    user = forms.CharField()

    def save(self):
        blog = Blog()
        blog.blog_title = self.cleaned_data['blog_title'] 
        blog.blog_text = self.cleaned_data['blog_text'] 
        blog.user = self.cleaned_data['user'] 
        blog.save()

class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea())
    score = forms.IntegerField()
    user = forms.CharField() 

    def save(self, blog_id):
        comment = Comment()
        comment.comment_text = self.cleaned_data['comment_text'] 
        comment.score = self.cleaned_data['score'] 
        comment.user = self.cleaned_data['user'] 
        comment.blog = get_object_or_404(Blog, pk=blog_id)
        comment.save()