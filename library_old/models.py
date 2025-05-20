from library.archive import archive
from library.base_models import BookStorage, CompositeBookStorage
from library.exceptions import BookComparisonNotAllowed, BookStorageIsFull


class Book:
    """Книга"""

    def __init__(self, title: str, uid: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.uid = uid
        self.year = year

    def __eq__(self, obj: object) -> bool:
        """
        Магический метод для сравнения книг. Сравниваем книги по uid

        :param obj: Объект для сравнения
        :return: Равны ли объекты
        :raises BookComparisonNotAllowed: Ошибка о сравнении книги с объектом другого типа
        """
        if not isinstance(obj, Book):
            raise BookComparisonNotAllowed()

        return self.uid == obj.uid

    def __str__(self) -> str:
        return f'№{self.uid} {self.author} "{self.title}" {self.year}г.'

    def __repr__(self) -> str:
        return str(self)


class Archive(BookStorage):
    """Архив"""

    def __init__(self) -> None:
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    @property
    def books(self) -> list[Book]:
        return self._books


class Shelf(BookStorage):
    """Полка"""

    def __init__(self, archive: BookStorage, limit: int = 10) -> None:
        self._limit = limit
        self._books = []
        self._archive = archive

    @property
    def is_available(self) -> bool:
        return len(self._books) < self._limit

    def add_book(self, book: Book) -> None:
        if not self.is_available:
            raise BookStorageIsFull()

        self._books.append(book)

    @property
    def books(self) -> list[Book]:
        return self._books

    def remove_book(self, book: Book) -> None:
        if book in self._books:
            self._books.remove(book)

    def archive_books(self, year: int) -> None:
        for book in (b for b in self._books if b.year < year):
            self._books.remove(book)
            self._archive.add_book(book)

    def remove_all_books(self) -> None:
        self._books = []

    def __str__(self) -> str:
        books_str = ", ".join(str(book) for book in self._books)
        return f"Полка с книгами: {books_str}"

    def __repr__(self) -> str:
        return str(self)


class Rack(CompositeBookStorage):
    """Стеллаж"""

    def _init_storages(self) -> None:
        self._storages = [Shelf(archive) for _ in range(self._limit)]

    def __str__(self) -> str:
        storages_str = ""
        for storage in self._storages:
            storages_str += f"\t- {storage}\n"

        return f"Стеллаж:\n{storages_str}"

    def __repr__(self) -> str:
        return str(self)


class Hall(CompositeBookStorage):
    """Зал"""

    def _init_storages(self) -> None:
        self._storages = [Rack(archive) for _ in range(self._limit)]

    def __str__(self) -> str:
        storages_str = ""
        for storage in self._storages:
            storages_str += f"- {storage}\n"

        return f"Зал:\n{storages_str}"

    def __repr__(self) -> str:
        return str(self)


class Library(CompositeBookStorage):
    """Библиотека"""

    def add_book(self, book) -> None:
        if not self.get_available_storage():
            self._storages.append(Hall(archive))
        super().add_book(book)

    def _init_storages(self) -> None:
        self._storages = [Hall(archive)]

    def __str__(self) -> str:
        storages_str = ""
        for storage in self._storages:
            storages_str += f"- {storage}\n"

        return f"Библиотека:\n{storages_str}"

    def __repr__(self) -> str:
        return str(self)
