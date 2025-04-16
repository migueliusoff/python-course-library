import pytest

from library.models import Hall
from library.tests.test_shelf import generate_books


def test_add_books_success():
    hall = Hall()
    books = generate_books(hall.get_free_space())
    hall.add_books(*books)
    assert hall.get_free_space() == 0


def test_add_books_fail():
    hall = Hall()
    books = generate_books(hall.get_free_space() + 1)
    with pytest.raises(ValueError) as error:
        hall.add_books(*books)
    assert str(error.value) == "Закончилось место для книг"
