import operator
from uuid import uuid4

import pytest

from library.archive import archive
from library.exceptions import CompositeBookStorageIsFull
from library.models import Book, Library, Rack


@pytest.fixture
def library() -> Library:
    return Library(archive)


@pytest.fixture
def rack() -> Rack:
    return Rack(archive)


def test_add_book_success(default_book, library: Library):
    book = default_book()
    library.add_book(book)

    assert book in library.books


@pytest.mark.parametrize("add_book", (True, False))
def test_remove_book(add_book: bool, library: Library, default_book):
    book = default_book()

    if add_book:
        library.add_book(book)

    library.remove_book(book)
    assert book not in library.books


def test_add_storage_success(library: Library, rack: Rack, default_book):
    for _ in range(1000):
        library.add_book(default_book())

    library.add_storage(rack)
    assert library.get_available_storage() == rack


def test_add_storage_error(library):
    with pytest.raises(CompositeBookStorageIsFull):
        for _ in range(10):
            library.add_storage(Rack(archive))


def test_add_book_with_creation_rack(library: Library, default_book):
    for _ in range(1000):
        library.add_book(default_book())

    assert not library.get_available_storage()

    library.add_book(default_book())
    assert library.get_available_storage()


def test_archive_books(library: Library, default_book):
    for i in range(2000, 2025):
        library.add_book(default_book(i))

    library.archive_books(2015)
    assert len(archive.books) == 15


def test_sort_books(library: Library):
    books = [Book(f"{10 - i}", str(uuid4()), "Test", 2025 - i % 3) for i in range(10)]
    for book in books:
        library.add_book(book)

    sorted_books = sorted(books, key=operator.attrgetter("year", "title"))
    assert library.books[0] != sorted_books[0]
    library.sort()
    assert library.books[0] == sorted_books[0]


def test_optimize(library: Library):
    books = [Book("Test", str(i), "Test", 2025) for i in range(100)]
    for book in books:
        library.add_book(book)

    for book in books:
        if int(book.uid) % 10 == 0:
            library.remove_book(book)

    assert len(library.get_available_storage().get_available_storage().get_available_storage().books) != 0
    library.sort()
    assert len(library.get_available_storage().get_available_storage().get_available_storage().books) == 0
