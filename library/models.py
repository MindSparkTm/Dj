# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from user.models import CustomUser
from django.urls import reverse
# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampedModel):
    name = models.CharField(_('Category Name'),max_length=50)

    class Meta:
        verbose_name = ('Category')
        verbose_name_plural = ('Categories')


    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('library:category_detail_view',kwargs={'pk':self.pk})


class Author(TimeStampedModel):
    first_name = models.CharField(_('First Name'),max_length=50)
    last_name = models.CharField(_('Last Name'),max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name = ('Author')
        verbose_name_plural = ('Authors')

    def __unicode__(self):
        return u'{}{}'.format(self.first_name,self.last_name)

    def get_absolute_url(self):
        return reverse('library:author_detail',kwargs={'pk':self.pk})


class Publisher(TimeStampedModel):
    name = models.CharField(_('Publisher Name'),max_length=50)
    address = models.CharField(_('Address'),max_length=100)
    state = models.CharField(_('State'),max_length=50)
    city = models.CharField(_('City'),max_length=50)
    country = models.CharField(_('Country'),max_length=60)

    def __unicode__(self):
        return self.name

class BookManager(models.Manager):

    def get_book_by_id(self, book_id):
        return self.get_queryset().filter(pk=book_id)

class Book(TimeStampedModel):

    title = models.CharField(_('Title of Book'),max_length=100)
    authors = models.ManyToManyField(Author)
    book_cover_image = models.ImageField(upload_to='images/',blank=True,null=True)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()
    categories = models.ForeignKey(Category)
    read_by = models.ManyToManyField(CustomUser,related_name='books')


    def __unicode__(self):
        return u'{}{}'.format(self.title,self.publication_date)
        
    def get_absolute_url(self):
        return reverse('library:book_detail',kwargs={'pk':self.pk})

    @classmethod
    def get_book_by_id(self,pk):
        try:
            book = Book.objects.get(id=pk)
        except Exception as ex:
            return
        else:
            return book

    @property
    def publisher_name(self):
        return self.publisher.name

    @property
    def authors_name(self):
        return self.authors.first_name

class Review(TimeStampedModel):
    comment = models.TextField(_('Enter your comment'))
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name='reviews')

    def __unicode__(self):
        return self.comment
