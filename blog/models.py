from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from froala_editor.fields import FroalaField

from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True)
    categoryImage = models.ImageField(upload_to="category_images/", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='featured_images/')
    content =  FroalaField()
    slug = models.SlugField(unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Contact(models.Model):
    FirstName = models.CharField(max_length=65)
    LastName = models.CharField(max_length=65, blank=True, null=True)
    email = models.EmailField()
    phone = PhoneNumberField()
    message = models.TextField(max_length=500)
    timestamp = models.DateField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.FirstName} {self.email} {self.phone} {self.message} {self.timestamp} {self.read}"