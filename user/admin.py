# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,TestUser,UserStatus

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

class UserStatusAdmin(admin.ModelAdmin):
    def get_user(self,obj):
        return obj.current_user.username
    list_display = ["get_user","session_id"]
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(TestUser)
admin.site.register(UserStatus,UserStatusAdmin)