from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=512)
    author_full_name = models.CharField(max_length=512)
    year_of_publishing = models.SmallIntegerField()
    copies_printed = models.IntegerField()
    short_description = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} ({self.author_full_name})"

    def to_json(self) -> dict[str, int | str]:
        return {
            "id": self.pk,
            "title": self.title,
            "author_full_name": self.author_full_name,
            "year_of_publishing": self.year_of_publishing,
            "copies_printed": self.copies_printed,
            "short_description": self.short_description,
        }


def get_book_by_id(book_id: int) -> Book | None:
    try:
        return Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return None
