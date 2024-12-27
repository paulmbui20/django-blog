
from django.urls import path

from . import views
from .views import BlogPostListView, BlogPostDetailView

urlpatterns = [
    path('', BlogPostListView, name='blogpost_list'),
    path('search/', views.search_posts, name='search_posts'),
    path('<slug:slug>/', BlogPostDetailView, name='blogpost_detail'),

]
