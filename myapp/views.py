from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect, reverse
from django.http import HttpResponse, Http404
from .models import Blog, Comment, UserProfile
from .forms import BlogForm, CommentForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import logout

def index(request):
    blog_list = Blog.objects.all().order_by('-updated_on')[:5]
    context = { 'blog_list' : blog_list }
    return render(request, 'myapp/index.html', context)

def new_blog(request):
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return redirect('index')
    else:
        form = BlogForm()
    context['form'] = form
    return render(request, 'myapp/new_blog.html', context)
    
def detail(request, blog_id):
    context = {}
    # comment in blog
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(blog_id, request.user)
            # clear form fields after submit.
            return redirect('detail', args=(blog_id,))
    else:
        form = CommentForm()
        context['form'] = form
        blog = get_object_or_404(Blog, pk=blog_id)
        context['blog'] = blog
        context['star_num'] = range(5)
        return render(request, 'myapp/detail.html', context)

def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    context = {}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(request.user, blog)
            return redirect('index')
    else:
        data = {'blog_title' : blog.blog_title, 'blog_text' : blog.blog_text, 'user' : blog.user}
        form = BlogForm(data)
        context['form'] = form
        return render(request, 'myapp/edit_blog.html', context)

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id, user=request.user)
    blog.delete()
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('index')

def profile(request, blog_user):
    context = {}
    user = get_object_or_404(User, username=blog_user)
    user_profile = UserProfile.objects.get(user=user)
    blogs = Blog.objects.filter(user=user)
    context['blogs'] = blogs
    context['user_profile'] = user_profile
    return render(request, 'myapp/profile.html' , context)

def edit_image(request, blog_user):
    context = {}
    user = get_object_or_404(User, username=blog_user)
    if user == request.user:
        if request.method == 'POST':
            userProfile = UserProfile.objects.get(user=user)
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(request.user, userProfile)
        else:
            form = UserProfileForm()
            context['form'] = form
            context['user'] = user
            return render(request, 'myapp/edit_image.html', context)
    else:
        raise Http404
    return redirect('index')