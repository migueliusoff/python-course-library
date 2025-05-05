import pytest

from library.archive import archive
from library.exceptions import BookStorageIsFull
from library.models import Shelf


def test_book_add_success(default_book):
    shelf = Shelf(archive)
    book = default_book()
    shelf.add_book(book)

    assert book in shelf.books


def test_book_add_error(default_book):
    shelf = Shelf(archive)
    with pytest.raises(BookStorageIsFull):
        for _ in range(11):
            shelf.add_book(default_book())


@pytest.mark.parametrize("add_book", (True, False))
def test_remove_book(add_book: bool, default_book):
    shelf = Shelf(archive)
    book = default_book()

    if add_book:
        shelf.add_book(book)

    shelf.remove_book(book)
    assert book not in shelf.books
