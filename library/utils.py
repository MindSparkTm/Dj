from .models import FileUpload,Author,Category,Publisher,Book
from django.conf import settings
import csv

def parse_uploaded_file(instance):
    try:
        file = FileUpload.objects.get(id=instance)
    except:
        return
    else:
        file_name = str(file.document)
        with open(settings.MEDIA_URL+'/'+file_name,'r') as f:
            author_list=[]
            f.readline()
            csv_reader = csv.DictReader(f)
            headers = csv_reader.fieldnames
            for line in csv_reader:
                title = line['title']
                authors = line['authors'].split(',')
                for author in authors:
                    if author:
                        author_first_name, author_last_name = author.split()
                        author_obj = author_is_in_db(author_first_name, author_last_name)
                        author_list.append(author_obj)
                publisher = publisher_is_in_db(line['publisher'])
                category = category_is_in_db(line['category'])
                publication_date = line['publication_date']
                book = book_is_in_db(title,publisher,publication_date,
                                     category)
                for author in author_list:
                    book.authors.add(author)
                    book.save()

def author_is_in_db(first_name,last_name):
    try:
        author = Author.objects.get(first_name=first_name,last_name=last_name)
    except Author.DoesNotExist:
        author = Author.objects.create(first_name=first_name,last_name=last_name)
        return author
    else:
        return author

def publisher_is_in_db(name):
    try:
        publisher = Publisher.objects.get(name=name)
    except Publisher.DoesNotExist:
        publisher = Publisher.objects.create(name=name)
        return publisher
    else:
        return publisher

def category_is_in_db(name):
    try:
        category = Category.objects.get(name=name)
    except Category.DoesNotExist:
        category = Category.objects.create(name=name)
        return category
    else:
        return category


def book_is_in_db(title,publisher,publication_date,category):
    try:
        book = Book.objects.get(title=title,publisher=publisher,publication_date=publication_date,category=category)
    except Book.DoesNotExist:
        book = Book.objects.create(title=title,publisher=publisher,
                                   publication_date=publication_date,category=category)
        return book
    else:
        return book
