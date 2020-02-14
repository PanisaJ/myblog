from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog, Comment

def index(request):
    #blogs = Blog.objects.order_by('-updated_on')[:5]
    blog_list = Blog.objects.order_by('-updated_on')[:5]
    context = { 'blog_list' : blog_list }
    return render(request, 'myapp/index.html', context)

def new_blog(request):
    return HttpResponse('new blog')