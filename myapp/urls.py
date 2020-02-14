from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_blog/', views.get_blog, name='getblog'),
    path('<int:blog_id>', views.detail, name='detail')
]