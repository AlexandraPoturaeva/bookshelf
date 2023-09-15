from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from books.models import Book


def all_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'all_books.html', context={'books': books})


def book_view(request: HttpRequest, book_id: int) -> HttpResponse | HttpResponseNotFound:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponseNotFound()

    return render(request, 'book.html', context={'book': book})