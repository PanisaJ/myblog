from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Blog, Comment
from .forms import BlogForm, CommentForm

def index(request):
    blog_list = Blog.objects.order_by('-updated_on')[:5]
    context = { 'blog_list' : blog_list }
    return render(request, 'myapp/index.html', context)

def get_blog(request):
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'myapp/index.html', { 'blog_list' : Blog.objects.order_by('-updated_on')[:5] })
        else:
            context['error_message'] = "You didn't insert some input."
    else:
        form = BlogForm()
    context['blog_list'] = Blog.objects.order_by('-updated_on')[:5]
    context['form'] = form
    return render(request, 'myapp/new_blog.html', context)
    
def detail(request, blog_id):
    context = {}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(blog_id)
        else:
            context['error_message'] = "You didn't insert some input."
    else:
        form = CommentForm()
    blog = get_object_or_404(Blog, pk=blog_id)
    context['blog'] = blog
    context['form'] = form
    context['star_num'] = range(5)
    return render(request, 'myapp/detail.html', context)

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    data = {'blog_title' : blog.blog_title, 'blog_text' : blog.blog_text, 'user' : blog.user}
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST, data)
        if form.is_valid():
            form.save()
            context['blog'] = blog
            context['form'] = form
            return render(request, 'myapp/detail.html', context)
        else:
            context['error_message'] = "You didn't edit some input."
    else:
        form = BlogForm(data)
    context['form'] = form
    return render(request, 'myapp/edit_blog.html', context)

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect('index')
