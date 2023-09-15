from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from books.models import Book


def all_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'all_books.html', context={'books': books})
