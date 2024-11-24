from django.contrib import admin
from .models import BlogPost, Category

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('status', 'categories')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, 'Selected posts have been published.')

    publish_posts.short_description = 'Publish selected posts'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
