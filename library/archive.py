from library.base_models import BookStorage


class Archive(BookStorage):
    """Архив"""

    def __init__(self) -> None:
        self._books = []

    def add_book(self, book) -> None:
        self._books.append(book)

    @property
    def books(self) -> list:
        return self._books


archive = Archive()
