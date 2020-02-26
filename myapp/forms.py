from django import forms
from django_starfield import Stars
from .models import Blog, Comment, CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blog_title', 'blog_text']

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', 'user_rating']
        widgets = { 'user_rating' : Stars }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
