import pytest

from library.models import Book, Shelf


def generate_books(count: int) -> list[Book]:
    return [Book("test", "test") for _ in range(count)]


def test_create_shelf_with_books_success():
    books = generate_books(3)
    shelf = Shelf(*books)
    assert shelf.books == books


def test_create_shelf_with_books_fail():
    books = generate_books(13)
    with pytest.raises(ValueError) as error:
        Shelf(*books)
    assert str(error.value) == "На полке не может храниться больше 10 книг"


def test_add_book_success():
    books = generate_books(5)
    shelf = Shelf()
    shelf.add_books(*books)
    assert shelf.books == books


def test_add_book_fail():
    books = generate_books(15)
    with pytest.raises(ValueError) as error:
        shelf = Shelf()
        shelf.add_books(*books)

    assert str(error.value) == "На полке не может храниться больше 10 книг"
