from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.new_blog, name='new_blog'),
    path('detail/<int:blog_id>', views.detail, name='detail'),
    path('edit/<int:blog_id>', views.edit_blog, name='edit'),
    path('delete/<int:blog_id>', views.delete_blog, name='delete'),
    path('profile/<blog_user>', views.profile, name='profile'),
    path('profile/<blog_user>/edit_image/', views.edit_image, name='edit_image')
]