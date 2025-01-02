
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    categoryImage = models.ImageField(upload_to="category_images/", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to='featured_images/')
    content =  CKEditor5Field('Text', config_name='extends',null=True)
    slug = models.SlugField(unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='blog_posts')

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comment = models.TextField()
    name = models.CharField(max_length=65)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-created_at']

class AnalyticsData(models.Model):
    page_path = models.CharField(max_length=255)
    sessions = models.IntegerField()
    pageviews = models.IntegerField()
    absolute_url = models.URLField()
    last_updated = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.page_path


class Contact(models.Model):
    priority_choices = [
        ('normal', 'normal'),
        ('urgent', 'urgent'),
    ]
    FirstName = models.CharField(max_length=65)
    LastName = models.CharField(max_length=65, blank=True, null=True)
    email = models.EmailField(max_length=65)
    phone = PhoneNumberField()
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    priority = models.CharField(max_length=65, choices=priority_choices, default='normal')

    def __str__(self):
        return f"{self.FirstName} - {self.date} - {self.time}"