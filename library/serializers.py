from rest_framework import serializers
from .models import Book,Author


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ( 'first_name', 'last_name')

class BookSerializer(serializers.ModelSerializer):
    publisher_name = serializers.ReadOnlyField()
    authors = AuthorSerializer(read_only=True,many=True)

    class Meta:
        model = Book
        fields = ('title', 'authors', 'categories', 'publication_date', 'book_cover_image', 'publisher_name',)
