from django.db.models import Count

from core.models import Book, Library, Shelf


def add_book_to_library(library: Library, book: Book) -> None:
    shelf = library.get_available_shelf()
    book.shelf = shelf
    book.save()


def archive_books(library: Library, year: int) -> None:
    Book.objects.select_related("shelf__rack__hall__library").filter(
        shelf__rack__hall__library=library, published_on_year_lt=year
    ).update(shelf=None, archive=library.archive)


def sort_books(library: Library) -> None:
    books = Book.objects.filter(library=library).order_by("published_on_year", "title")
    books.update(shelf=None)
    for book in books:
        add_book_to_library(library, book)


def optimize_library(library: Library) -> None:
    shelves = tuple(Shelf.objects.annotate(books_count=Count("books")).filter(books_count__lt=10))
    books = Book.objects.filter(shelf__in=shelves)
    books.update(shelf=None)
    books = tuple(books)
    offset = 0
    for shelf in shelves:
        for book in books[offset : offset + 10]:
            book.shelf = shelf
            book.save()
        offset += 10
        if offset > len(books):
            break
