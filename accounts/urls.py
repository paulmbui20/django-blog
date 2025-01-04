import profile

from django.conf.urls.static import static
from django.urls import path

from blog import views
from blog.views import add_post, update_post_status, add_category, analytics_dashboard
from djangoBlog import settings
from .views import register, account, logout_view, update_password, update_image, delete_image, profile, queries, \
    delete_contact_query, update_email
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('',account, name='account'),
    path('edit-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('add/', add_post, name='add_post'),
    path('add-category', add_category, name='add_category'),

    path('edit-category/<str:slug>/', views.edit_category, name='edit_category'),

    path('analytics/', analytics_dashboard, name='analytics_dashboard'),

    path('profile/',profile, name='profile'),
    path('profile/update-password/', update_password, name='update_password'),
    path('profile/update-email/', update_email, name='update_email'),
    path('profile/update-image/', update_image, name='update_image'),
    path('profile/delete-image/', delete_image, name='delete_image'),

    path('update_post_status/', update_post_status, name='update_post_status'),

    path('queries', queries, name='queries'),

    path('delete_contact_query/', delete_contact_query, name='delete_contact_query'),

]