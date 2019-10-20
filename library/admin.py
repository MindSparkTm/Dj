# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Category, Author, Publisher, Book, Review, FileUpload,chatmessage


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', 'last_modified')
    readonly_fields = ('created', 'last_modified')
    search_fields = ('name',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    list_filter = ('email', 'last_modified')
    readonly_fields = ('created', 'last_modified')
    search_fields = ('first_name', 'email')


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'state', 'country')
    list_filter = ('name', 'country', 'last_modified')
    readonly_fields = ('created', 'last_modified')
    search_fields = ('name', 'country')


class BookAdmin(admin.ModelAdmin):
    def get_publisher(self, obj):
        return obj.publisher.name

    list_display = ('title', 'get_publisher')
    list_filter = ('title', 'last_modified')
    readonly_fields = ('created', 'last_modified')
    search_fields = ('name', 'get_publisher')

class ChatMessageAdmin(admin.ModelAdmin):
    def get_user(self, obj):
        return obj.user_id.username
    list_display = ('message_text', 'get_user','group_name')
    readonly_fields = ('created', 'last_modified')
    search_fields = ('get_user','group_name',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(FileUpload)
admin.site.register(chatmessage,ChatMessageAdmin)
