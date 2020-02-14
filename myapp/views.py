from django.shortcuts import get_object_or_404, render
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
            newform = form.save(commit=False)
            newform.blog = Blog.objects.get(pk=blog_id) 
            newform.save()  
        else:
            context['error_message'] = "You didn't insert some input."
    else:
        form = CommentForm()
    blog = get_object_or_404(Blog, pk=blog_id)
    context['blog'] = blog
    context['form'] = form
    return render(request, 'myapp/detail.html', context)