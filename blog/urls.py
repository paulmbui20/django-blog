from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.urls.conf import include

from . import views
from .views import BlogPostListView, BlogPostDetailView, category_view

urlpatterns = [
    path('', BlogPostListView, name='blogpost_list'),
    path('search/', views.search_posts, name='search_posts'),
    path('<slug:slug>/', BlogPostDetailView, name='blogpost_detail'),
]
