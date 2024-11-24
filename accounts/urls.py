from django.urls import path

from blog import views
from blog.views import add_post
from .views import register, account, logout_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('',account, name='account'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add/', add_post, name='add_post'),
]