from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True, choices=(('M', 'Male'), ('F', 'Female')))
    image = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    website = models.URLField(max_length=65, blank=True, null=True)
    slug = models.SlugField(max_length=65, unique=True, null=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
