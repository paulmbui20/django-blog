from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts import views
from djangoBlog.views import index, author, authors_list_view, category_list_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('blog.urls')),
    path('author/<slug:slug>/', author, name='author'),
    path('authors/', authors_list_view, name='authors_list'),
    path('categories/', category_list_view, name='category_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)