from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from books.models import Book, get_book_by_id


def all_books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'all_books.html', context={'books': books})


def book_view(request: HttpRequest, book_id: int) -> HttpResponse | HttpResponseNotFound:
    book = get_book_by_id(book_id)

    if not book:
        return HttpResponseNotFound()

    return render(request, 'book.html', context={'book': book})


def all_books_details_handler(request: HttpRequest) -> JsonResponse:
    books = Book.objects.all()
    data = [book.get_book_details() for book in books]

    return JsonResponse(
        {'all_books_details': data},
        json_dumps_params={'ensure_ascii': False}
    )


def one_book_details_handler(request: HttpRequest, book_id: int) -> HttpResponseNotFound | JsonResponse:
    book = get_book_by_id(book_id)

    if not book:
        return HttpResponseNotFound()

    return JsonResponse(
        book.get_book_details(),
        json_dumps_params={'ensure_ascii': False}
    )
