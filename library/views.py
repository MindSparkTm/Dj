# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView
from django.views.generic.list import ListView
from .models import *
from django.shortcuts import redirect,get_object_or_404
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .serializers import BookSerializer
# Create your views here.


class CategoryListView(ListView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'

    def get_context_data(self,**kwargs):
        ctx = super(CategoryCreateView,self).get_context_data(**kwargs)
        ctx['custom_heading'] = 'Create a Category'
        return ctx

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'library/category_detail.html'

class CategoryUpdateView(UpdateView):
    model = Category
    fields =['name']

    def get_context_data(self,**kwargs):
        ctx = super(CategoryUpdateView,self).get_context_data(**kwargs)
        ctx['custom_heading'] = 'Update Category'
        return ctx

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('library:category_list_view')
    def get_context_data(self,**kwargs):
        ctx = super(CategoryDeleteView,self).get_context_data(**kwargs)
        ctx['custom_heading'] = 'Delete Category'
        return ctx

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

    def get_context_data(self,**kwargs):
        ctx = super(AuthorCreate,self).get_context_data(**kwargs)
        ctx['author_heading'] = 'Create a New Author'
        return ctx

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model  = Author
    template_name = 'library/author_detail.html'

class AuthorUpdate(UpdateView):
    model  = Author
    fields = '__all__'

    def get_context_data(self,**kwargs):
        ctx = super(AuthorUpdate,self).get_context_data(**kwargs)
        ctx['author_heading'] = 'Update Author'
        return ctx
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('library:author_list')

    def get_context_data(self,**kwargs):
        ctx = super(AuthorDelete,self).get_context_data(**kwargs)
        ctx['author_heading'] = 'Delete Author'
        return ctx

class PublisherCreate(CreateView):
    model = Publisher
    fields = '__all__'

    def get_context_data(self,**kwargs):
        ctx = super(PublisherCreate,self).get_context_data(**kwargs)
        ctx['publisher_heading'] = 'Create a New Publisher'
        return ctx

class PublisherList(ListView):
    model = Publisher

class PublisherDetail(DetailView):
    model  = Publisher
    template_name = 'library/publisher_detail.html'

class PublisherUpdate(UpdateView):
    model  = Publisher
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('library:publisher_detail',kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self,**kwargs):
        ctx = super(PublisherUpdate,self).get_context_data(**kwargs)
        ctx['publisher_heading'] = 'Update Publisher'
        return ctx

class PublisherDelete(DeleteView):
    model = Publisher
    success_url = reverse_lazy('library:publisher_list')

    def get_context_data(self,**kwargs):
        ctx = super(PublisherDelete,self).get_context_data(**kwargs)
        ctx['publisher_heading'] = 'Delete Publisher'
        return ctx

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = ('title','authors','categories','publication_date','book_cover_image','publisher',)

    def get_context_data(self,**kwargs):
        ctx = super(BookCreate,self).get_context_data(**kwargs)
        ctx['book_heading'] = 'Add a new Book'
        return ctx

class BookDetail(DetailView):
    model = Book
    template_name = 'library/book_detail.html'

    def get_context_data(self,**kwargs):
        ctx = super(BookDetail,self).get_context_data(**kwargs)
        ctx['book_heading'] = 'Book Details'
        qs = Book.objects.filter(read_by=self.request.user,id=self.kwargs['pk'])
        print('qs',qs)
        if qs:
            ctx['read_by_user'] = True
        else:
            ctx['read_by_user'] = False
        return ctx

class BookUpdate(UpdateView):
    model  = Book
    fields = ('title','authors','categories','publication_date','book_cover_image','publisher',)

    def get_context_data(self,**kwargs):
        ctx = super(BookUpdate,self).get_context_data(**kwargs)
        ctx['book_heading'] = 'Update Book'
        return ctx

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('library:book_list')

    def get_context_data(self,**kwargs):
        ctx = super(BookDelete,self).get_context_data(**kwargs)
        ctx['book_heading'] = 'Delete Book'
        return ctx

class ReviewCreate(CreateView):
    model = Review
    fields = ('comment',)

    def get_context_data(self,**kwargs):
        ctx = super(ReviewCreate,self).get_context_data(**kwargs)
        ctx['comment_heading'] = 'Create your Comment'
        return ctx

    def form_valid(self, form):
        book = get_object_or_404(Book,pk=self.kwargs['pk'])
        user = get_object_or_404(CustomUser,pk=self.request.user.id)
        review = Review(book=book,comment=form.cleaned_data['comment'],user=user)
        review.save()
        return redirect(reverse_lazy('library:book_detail',kwargs={'pk':self.kwargs['pk']}))


class ReviewUpdate(UpdateView):
    model = Review
    fields = ('comment',)

    def get_success_url(self,**kwargs):
        return reverse_lazy('library:book_list')

    def get_context_data(self,**kwargs):
        ctx = super(ReviewUpdate,self).get_context_data(**kwargs)
        ctx['comment_heading'] = 'Update your Comment'
        return ctx

class ReviewDelete(DeleteView):
    model = Review

    def get_success_url(self,**kwargs):
        return reverse_lazy('library:book_list')

    def get_context_data(self,**kwargs):
        ctx = super(ReviewDelete,self).get_context_data(**kwargs)
        ctx['comment_heading'] = 'Delete your Comment'
        return ctx

class ReadBookList(ListView):
    model = Book
    template_name = 'library/read_book_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(ReadBookList,self).get_context_data(**kwargs)
        ctx['book_list'] = 'Books you Read'
        return ctx

    def get_queryset(self):
        return Book.objects.filter(read_by=self.request.user)

#DRF section


class BookListApi(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

#End of DRF section

@csrf_exempt
def book_mark_read(request):
    if request.is_ajax() and request.POST['book_id']:
        book_id = request.POST.get('book_id','None')
        book = Book.get_book_by_id(book_id)
        if book is not None:
            book.read_by.add(request.user)
            return HttpResponse('success')
        else:
            return HttpResponse('failure')
    else:
        return HttpResponse('Error')