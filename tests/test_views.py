from django.test import TestCase
from django.urls import reverse
from books.models import Book


class BookViewTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        number_of_books = 5

        for book_id in range(1, number_of_books + 1):
            Book.objects.create(
                title=f'Книга {book_id}',
                author_full_name=f'Автор книги {book_id}',
                year_of_publishing=2000 + book_id,
                copies_printed=book_id * 10,
                short_description=f'Описание книги {book_id}',
                )

    def test_all_books_view_url_exists_at_desired_location(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_all_books_view_uses_correct_template(self):
        response = self.client.get(reverse('all_books'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'all_books.html')

    def test_one_book_url_exists_at_desired_location_by_id(self):
        response = self.client.get('/books/3/')
        self.assertEqual(response.status_code, 200)

    def test_one_book_view_not_found(self):
        response = self.client.get('/books/7/')
        self.assertEqual(response.status_code, 404)

    def test_one_book_view_uses_correct_template(self):
        response = self.client.get(reverse('one_book', kwargs={'book_id': 3}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book.html')

    def test_one_book_details_handler_return_correct_json(self):
        book_id = 2
        expected_json = {
            "id": book_id,
            "title": f'Книга {book_id}',
            "author_full_name": f'Автор книги {book_id}',
            "year_of_publishing": 2000 + book_id,
            "copies_printed": book_id * 10,
            "short_description": f'Описание книги {book_id}',
        }
        response = self.client.get(f'/api/books/{book_id}/')
        self.assertEqual(response.json(), expected_json)
