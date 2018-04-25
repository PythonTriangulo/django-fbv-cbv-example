import csv
from myproject.core.models import Book


book_list = []

with open('fix/books.csv') as f:
    books = csv.DictReader(f)
    for book in books:
        book_list.append(
            Book(
                title=book['BookTitle'],
                author=book['BookAuthor'],
                year_publication=book['YearOfPublication'],
                publisher=book['Publisher'],
                cover=book['ImageURL_L'],
            )
        )


Book.objects.bulk_create(book_list)
