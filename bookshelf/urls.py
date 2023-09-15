from django.contrib import admin
from django.urls import path

from books.views import all_books_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', all_books_view)
]
