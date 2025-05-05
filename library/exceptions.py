class LibraryException(Exception):
    """Базовая ошибка для проекта Library"""


class BookStorageIsFull(LibraryException):
    """
    В хранилище нет места для книги

    Сообщение по умолчанию - 'Закончилось место для книг'
    """

    def __init__(self, message: str = "Закончилось место для книг") -> None:
        super().__init__(message)


class CompositeBookStorageIsFull(LibraryException):
    """
    В составном хранилище нет места для нового хранилища

    Сообщение по умолчанию - 'Закончилось место для хранилищ'
    """

    def __init__(self, message: str = "Закончилось место для хранилищ") -> None:
        super().__init__(message)


class BookComparisonNotAllowed(LibraryException):
    """Ошибка для попытки сравнения книги с объектом другого типа"""

    def __init__(self, message: str = "Книгу можно сравнить только с книгой") -> None:
        super().__init__(message)
