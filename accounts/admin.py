from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from .models import CustomUser


admin.site.unregister(Group)


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, admin.ModelAdmin):
    pass