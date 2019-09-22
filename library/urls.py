from django.conf.urls import url
from .views import *

app_name = 'library'
urlpatterns = [
# category urls
url(r'category/$', CategoryListView.as_view(), name='category_list_view'),
url(r'category/add/$', CategoryCreateView.as_view(), name='category_create_view'),
url(r'category/(?P<pk>\w+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
url(r'category/(?P<pk>\w+)/edit/$', CategoryUpdateView.as_view(), name='category_update_view'),
url(r'category/(?P<pk>\w+)/delete/$',CategoryDeleteView.as_view(),name='category_delete_view'),

# Author urlpatterns
url(r'author/$', AuthorList.as_view(), name='author_list'),
url(r'author/add/$', AuthorCreate.as_view(), name='author_create'),
url(r'author/(?P<pk>\w+)/$', AuthorDetail.as_view(), name='author_detail'),
url(r'author/(?P<pk>\w+)/edit/$', AuthorUpdate.as_view(), name='author_update'),
url(r'author/(?P<pk>\w+)/delete',AuthorDelete.as_view(), name='author_delete'),

# Publisher urlpatterns
url(r'publisher/$', PublisherList.as_view(), name='publisher_list'),
url(r'publisher/add/$', PublisherCreate.as_view(), name='publisher_create'),
url(r'publisher/(?P<pk>\w+)/$', PublisherDetail.as_view(), name='publisher_detail'),
url(r'publisher/(?P<pk>\w+)/edit/$', PublisherUpdate.as_view(), name='publisher_update'),
url(r'publisher/(?P<pk>\w+)/delete',PublisherDelete.as_view(), name='publisher_delete'),

# Book urlpatterns
url(r'book/$', BookList.as_view(), name='book_list'),
url(r'book/add/$', BookCreate.as_view(), name='book_create'),
url(r'book/(?P<pk>\w+)/$', BookDetail.as_view(), name='book_detail'),
url(r'book/(?P<pk>\w+)/edit/$', BookUpdate.as_view(), name='book_update'),
url(r'book/(?P<pk>\w+)/delete',BookDelete.as_view(), name='book_delete'),
url(r'book/collection/read$', ReadBookList.as_view(), name='read_book_list'),
url(r'book/mark/read/$', book_mark_read, name='mark_read'),

#Book REST API urls
url(r'book/api/v1/$', BookListApi.as_view(), name='api_book_list'),
url(r'book/api/v1/(?P<pk>\w+)/$', BookDetailApi.as_view(), name='api_book_detail'),

# review urlpatterns
url(r'review/add/(?P<pk>\w+)/$', ReviewCreate.as_view(), name='review_create'),
url(r'review/(?P<pk>\w+)/edit/$', ReviewUpdate.as_view(), name='review_update'),
url(r'review/(?P<pk>\w+)/delete/$', ReviewDelete.as_view(), name='review_delete'),


]
