import profile

from django.urls import path

from blog import views
from blog.views import add_post
from .views import register, account, logout_view, update_password, update_image, delete_image, profile_edit, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('',account, name='account'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add/', add_post, name='add_post'),

    path('profile/',profile, name='profile'),
    path('profile/edit/<int:user_id>', profile_edit, name='profile_edit'),
    path('profile/update-password/<int:user_id>/', update_password, name='update_password'),
    path('profile/update-image/<int:user_id>/', update_image, name='update_image'),
    path('profile/delete-image/<int:user_id>/', delete_image, name='delete_image'),

]