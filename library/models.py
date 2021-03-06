# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from user.models import CustomUser
from django.urls import reverse
from django.contrib.sessions.models import Session


# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(_('Category Name'), max_length=50)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:category_detail_view', kwargs={'pk': self.pk})


class Author(TimeStampedModel):
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    email = models.EmailField(null=True,blank=True)

    class Meta:
        verbose_name = ('Author')
        verbose_name_plural = ('Authors')

    def __str__(self):
        return u'{}{}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('library:author_detail', kwargs={'pk': self.pk})


class Publisher(TimeStampedModel):
    name = models.CharField(_('Publisher Name'), max_length=50)
    address = models.CharField(_('Address'), max_length=100,null=True,blank=True)
    state = models.CharField(_('State'), max_length=50,null=True,blank=True)
    city = models.CharField(_('City'), max_length=50,null=True,blank=True)
    country = models.CharField(_('Country'), max_length=60,null=True,blank=True)

    def __str__(self):
        return self.name


class BookManager(models.Manager):

    def get_book_by_id(self, book_id):
        return self.get_queryset().filter(pk=book_id)


class Book(TimeStampedModel):
    title = models.CharField(_('Title of Book'), max_length=100)
    authors = models.ManyToManyField(Author)
    book_cover_image = models.ImageField(upload_to='images/', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    read_by = models.ManyToManyField(CustomUser, related_name='books')

    def __unicode__(self):
        return u'{}{}'.format(self.title, self.publication_date)

    def get_absolute_url(self):
        return reverse('library:book_detail', kwargs={'pk': self.pk})

    @classmethod
    def get_book_by_id(self, pk):
        try:
            book = Book.objects.get(id=pk)
        except Exception as ex:
            return
        else:
            return book

    @property
    def publisher_name(self):
        return self.publisher.name


class Review(TimeStampedModel):
    comment = models.TextField(_('Enter your comment'))
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __unicode__(self):
        return self.comment


class FileUpload(TimeStampedModel):
    document = models.FileField(upload_to='bulk_upload/')
    file_name = models.CharField(_('Add a file name'), max_length=50)

    def __str__(self):
        return u'{}'.format(self.file_name)

    def __unicode__(self):
        return u'{}'.format(self.file_name)

class chatmessage(TimeStampedModel):
    message_text = models.CharField(max_length=400,null=True,blank=True)
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='chat_user')
    group_name = models.CharField(max_length=50,default='others',null=True,blank=True)


