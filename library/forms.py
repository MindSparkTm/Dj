from .models import Book,Category,Author,Publisher,Review,FileUpload
from django import forms

class CategoryForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Category

class AuthorForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Author

class PublisherForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Publisher

class BookForm(forms.ModelForm):
    class Meta:
        fields = ('__all__')
        model = Book

class FileUploadForm(forms.ModelForm):
    class Meta:
        fields = ('__all__')
        model = FileUpload

