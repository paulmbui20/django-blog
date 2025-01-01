from django import forms
from django.contrib import admin

from .models import BlogPost, Category, Contact, Comment


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at','featured_image','categories', 'author')
    list_filter = ('status', 'categories')
    list_editable = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
    actions = ['publish_posts']
    list_per_page = 10

    def publish_posts(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, 'Selected posts have been published.')
    publish_posts.short_description = 'Publish selected posts'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug', 'categoryImage')
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 10
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment', 'blog_post__title', 'created_at')
    list_filter = ('created_at',)
    list_per_page = 10


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'phone', 'email', 'date','time', 'read', 'priority')
    search_fields = ('FirstName', 'LastName', 'message', 'email', 'phone')
    list_filter = ('read', 'date', 'priority')
    list_editable = ('read',)
    actions = ['read_contact']
    list_display_links = ('id','FirstName',)

    def read_contact(self, request, queryset):
        queryset.update(read=True)
        self.message_user(request, 'Selected contact have been read.')
    read_contact.short_description = 'Read selected contact'

