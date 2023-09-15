from django.contrib import admin
from django.urls import path

from books.views import all_books_view, book_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', all_books_view),
    path('books/<int:book_id>/', book_view)
]
