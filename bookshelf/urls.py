from django.contrib import admin
from django.urls import path

from books.views import all_books_view, all_books_details_handler, book_view, one_book_details_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', all_books_view, name='all_books'),
    path('books/<int:book_id>/', book_view, name='one_book'),
    path('api/books/', all_books_details_handler),
    path('api/books/<int:book_id>/', one_book_details_handler),
]
