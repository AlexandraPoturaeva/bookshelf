from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from books.models import Book
from typing import Dict


def get_book(book_id: int) -> Book | None:
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return None


def get_book_details(book: Book | None) -> Dict | None:
    if book:
        book_details = {
            "id": book.pk,
            "title": book.title,
            "author_full_name": book.author_full_name,
            "year_of_publishing": book.year_of_publishing,
            "copies_printed": book.copies_printed,
            "short_description": book.short_description,
        }
        return book_details

    return None

def all_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'all_books.html', context={'books': books},)


def book_view(request: HttpRequest, book_id: int) -> HttpResponse | HttpResponseNotFound:
    book = get_book(book_id)

    if book:
        return render(request, 'book.html', context={'book': book},)

    return HttpResponseNotFound()


def all_books_details_handler(request: HttpRequest) -> JsonResponse:
    books = Book.objects.all()
    data = [get_book_details(book) for book in books]

    return JsonResponse(
        {'all_books_details': data},
        json_dumps_params={'ensure_ascii': False},
    )


def one_book_details_handler(request: HttpRequest, book_id: int) -> HttpResponseNotFound | JsonResponse:
    book_details = get_book_details(get_book(book_id))

    if book_details:
        return JsonResponse(
            book_details,
            json_dumps_params={'ensure_ascii': False},
        )

    return HttpResponseNotFound()
