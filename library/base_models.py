import operator

from library.exceptions import CompositeBookStorageIsFull


class BookStorage:
    """Базовый класс для хранилища книг"""

    def add_book(self, book) -> None:
        """
        Добавляет книгу в хранилище

        :param book: Книга
        :raises BookStorageIsFull: Нет места в хранилище
        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    @property
    def is_available(self) -> bool:
        """
        Является ли хранилище доступным для добавления книги

        :return: Является ли доступным
        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    @property
    def books(self) -> list:
        """
        Книги в хранилище

        :return: Книги
        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    def remove_book(self, book) -> None:
        """
        Убрать книгу из хранилища

        :param book: Книга
        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    def archive_books(self, year: int) -> None:
        """
        Архивация. Все книги, год издания которых меньше определенного - переносят из залов в отдельное помещение,
        называемое архивом

        :param year: Год издания
        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    def sort(self) -> None:
        """
        Упорядочивание. Все книги, которые есть в залах - последовательно расставляют по году издания,
        внутри года - по названию

        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    def remove_all_books(self) -> None:
        """
        Удаление всех книг

        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError


class CompositeBookStorage(BookStorage):
    """
    Базовый класс для составного хранилища книг. Хранит в себе другие хранилища книг.
    Данный класс помогает реализовать паттерн Компоновщик
    """

    def __init__(self, archive: BookStorage, limit: int = 10) -> None:
        self._archive = archive
        self._storages: list[BookStorage] = []
        self._limit = limit
        self._init_storages()

    def _init_storages(self):
        """
        Автоматическая инициализация необходимой структуры хранилищ

        :raises NotImplementedError: Метод не реализован
        """

        raise NotImplementedError

    def add_storage(self, storage: BookStorage) -> None:
        """
        Добавляет хранилище

        :param storage: Хранилище
        :raises CompositeBookStorageIsFull: Нет места для нового хранилища
        """

        if len(self._storages) == self._limit:
            raise CompositeBookStorageIsFull()

        self._storages.append(storage)

    def get_available_storage(self) -> BookStorage | None:
        """
        Получить доступное хранилище

        :return: Хранилище
        """

        for storage in self._storages:
            if storage.is_available:
                return storage

        return None

    def add_book(self, book) -> None:
        if storage := self.get_available_storage():
            storage.add_book(book)

    @property
    def is_available(self) -> bool:
        return any(storage.is_available for storage in self._storages)

    @property
    def books(self) -> list:
        books = []
        for storage in self._storages:
            books.extend(storage.books)
        return books

    def remove_book(self, book) -> None:
        for storage in self._storages:
            if book in storage.books:
                storage.remove_book(book)

    def archive_books(self, year: int) -> None:
        books_to_archive = filter(lambda book: book.year < year, self.books)
        for book in books_to_archive:
            self.remove_book(book)
            self._archive.add_book(book)

    def remove_all_books(self) -> None:
        for storage in self._storages:
            storage.remove_all_books()

    def sort(self) -> None:
        sorted_books = sorted(self.books, key=operator.attrgetter("year", "title"))
        self.remove_all_books()
        for book in sorted_books:
            self.add_book(book)

    def optimize(self) -> None:
        """
        Оптимизация - все книги располагают таким образом, чтобы в каждом зале было как можно больше пустых полок
        """

        books = tuple(self.books)
        self.remove_all_books()

        for book in books:
            self.add_book(book)
