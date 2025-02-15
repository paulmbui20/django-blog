from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from blog.sitemaps import BlogPostSitemap
from blog.views import category_view, contact, contactform, commentform, deletecomment
from djangoBlog.views import index, author, authors_list_view, category_list_view, search

sitemaps = { 'posts': BlogPostSitemap, }
urlpatterns = [
    path('admin/', admin.site.urls),
     path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('allauth.urls')), # Django-allauth URLs
    path('posts/', include('blog.urls')),
    path('author/<slug:slug>/', author, name='author'),
    path('authors/', authors_list_view, name='authors_list'),
    path('categories/', category_list_view, name='category_list'),
    path('category/<slug:slug>/', category_view, name='category_detail'),

    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
    path('contactform/', contactform, name='contactform'),

    path('commentform/post/<str:slug>', commentform, name='commentform'),

    path('deletecomment/<int:pk>', deletecomment, name='deletecomment'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),

    path("ckeditor5/", include('django_ckeditor_5.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)