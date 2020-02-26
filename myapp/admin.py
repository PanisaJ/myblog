from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Blog, Comment, CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'profile_image']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Blog)
admin.site.register(Comment)