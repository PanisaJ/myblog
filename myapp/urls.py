from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('callback/', views.line_callback, name='callback'),
    path('new_blog/', views.BlogCreateView.as_view(), name='new_blog'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', views.BlogUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', views.BlogDeleteView.as_view(), name='delete'),
    path('signup', views.CustomUserCreateView.as_view(), name='signup'),
    path('logout', views.LogoutView.as_view(), name='logout_id'),
    path('<blog_user>/', views.ProfileDetailView.as_view(), name='profile'),
    path('<blog_user>/edit_image/', views.ImageUpdateView.as_view(), name='edit_image'),
    
]