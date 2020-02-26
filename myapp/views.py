from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, Http404
from .models import Blog, Comment, CustomUser
from .forms import BlogCreateForm, CommentCreateForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.views.generic.edit import FormMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class IndexView(ListView):
    queryset = Blog.objects.all().order_by('-updated_on')
    template_name = 'myapp/index.html'
    paginate_by = 3

class BlogCreateView(CreateView):
    template_name = "myapp/new_blog.html"
    form_class = BlogCreateForm

    def form_valid(self, form):
       blog = form.save(commit=False)
       blog.user = CustomUser.objects.get(username=self.request.user)
       blog.save()
       return redirect('index')

class BlogDetailView(FormMixin, DetailView):
    model = Blog
    template_name = "myapp/detail.html"
    form_class = CommentCreateForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = CustomUser.objects.get(username=self.request.user)
        comment.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_num'] = range(5)
        return context

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['blog_title', 'blog_text']
    template_name = "myapp/edit_blog.html"

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('index')

@method_decorator(csrf_exempt, name='dispatch')
class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "registration/logged_out.html")
        
class CustomUserCreateView(CreateView):
    model = CustomUser
    template_name = "myapp/signup.html"
    form_class = CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/signup.html', {'form' : form})

class ProfileDetailView(DetailView):
    template_name = "myapp/profile.html"
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['blog_user'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(user=self.object)
        context['blogs'] = blogs 
        return context
    
class ImageUpdateView(UpdateView):
    fields = ['profile_image']
    template_name = "myapp/edit_image.html"

    def get_object(self):
        return get_object_or_404(CustomUser, username=self.kwargs['blog_user'])

    