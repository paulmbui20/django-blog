
from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import BlogPost, Category, Contact


@admin.register(BlogPost)
class BlogPostAdmin(ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('status', 'categories')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, 'Selected posts have been published.')

    publish_posts.short_description = 'Publish selected posts'

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'FirstName', 'LastName', 'phone', 'email', 'message', 'timestamp', 'read')
    search_fields = ('FirstName', 'LastName', 'message')
    list_filter = ('read', 'timestamp')
