from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoBlog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)