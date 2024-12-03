from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(status='published')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return reverse('blogpost_detail', args=[obj.slug])
