# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import asyncio
from asgiref.sync import async_to_sync

from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.contrib.auth.signals import user_logged_in,user_logged_out
from django.contrib.sessions.models import Session
from channels.layers import get_channel_layer

# Create your models here.

class CustomUser(AbstractUser):

    def __str__(self):
        return self.email

class TestUser(AbstractBaseUser):

    def __str__(self):
        return self.get_username()

class UserStatus(models.Model):
    current_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,related_name='test_user')
    status = models.IntegerField(default=0)
    session_id = models.CharField(max_length=32, null=True, blank=True)


    def __str__(self):
        return u'{}{}'.format(self.current_user.first_name,self.session_id)

def user_logged_in_handler(sender, request, user, **kwargs):
    user_status = UserStatus.objects.filter(
        current_user=user,
    )
    if user_status:
        UserStatus.objects.filter(current_user=user).update(session_id=request.session.session_key,
               status=1
               )
    else:
        UserStatus.objects.create(
            current_user=user,
            session_id=request.session.session_key,
            status = 1
        )
    print('us',user.username)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "gossip", {"type": "user_gossip",
                   "event": "New User",
                   "username": user.username})

user_logged_in.connect(user_logged_in_handler)

def on_user_logged_out_handler(sender, **kwargs):
    UserStatus.objects.filter(current_user=kwargs.get('user')).delete()

user_logged_out.connect(on_user_logged_out_handler)