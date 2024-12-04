
from django.contrib import admin

from .models import BlogPost, Category, Contact


@admin.register(BlogPost)
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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'phone', 'email', 'message', 'timestamp', 'read')
    search_fields = ('FirstName', 'LastName', 'message')
    list_filter = ('read', 'timestamp')
    list_editable = ('read',)
    actions = ['read_comments']
    list_display_links = ('id','FirstName','message',)

    def read_comments(self, request, queryset):
        queryset.update(read=True)
        self.message_user(request, 'Selected comments have been read.')
    read_comments.short_description = 'Read selected comments'

