from library.mixins import BooksMixin


class Book:
    """Книга"""

    _book_index = 0

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.index = Book._book_index
        Book._book_index += 1

    def __str__(self) -> str:
        return f'№{self.index} {self.author} "{self.title}"'

    def __repr__(self) -> str:
        return str(self)


class Shelf:
    """Полка"""

    _book_limit = 10

    def __init__(self, *books: Book | None):
        if len(books) > Shelf._book_limit:
            raise ValueError("На полке не может храниться больше 10 книг")
        self._books = list(books)

    def add_books(self, *books: Book | None):
        """Добавление книг

        :param books: Книги
        :return:
        """
        if len(books) + len(self._books) > self._book_limit:
            raise ValueError("На полке не может храниться больше 10 книг")
        self._books.extend(books)

    def get_books(self):
        """Получение книг

        :return:
        """
        return self._books

    def remove_book(self, book: Book):
        self._books.remove(book)

    @classmethod
    def get_capacity(cls) -> int:
        """Узнать вмещаемость полки

        :return: Вмещаемость полки
        """
        return cls._book_limit

    def get_free_space(self) -> int:
        """Получить кол-во свободных мест на полке

        :return: Кол-во свободных мест
        """
        return self._book_limit - len(self._books)

    def __str__(self) -> str:
        books_str = ", ".join(str(book) for book in self._books)
        return f"Полка с книгами: {books_str}"

    def __repr__(self) -> str:
        return str(self)


class Rack(BooksMixin):
    """Стеллаж"""

    _place_to_put_attr = "_shelves"
    _shelf_limit = 10

    def __init__(self):
        self._shelves = [Shelf() for _ in range(Rack._shelf_limit)]

    @classmethod
    def get_capacity(cls) -> int:
        """Узнать вмещаемость стеллажа

        :return: Вмещаемость
        """
        return cls._shelf_limit * Shelf.get_capacity()

    def __str__(self) -> str:
        shelves_str = ""
        for shelf in self._shelves:
            if shelf.get_free_space() == Shelf.get_capacity():
                continue
            shelves_str += f"\t- {shelf}\n"

        return f"Стеллаж:\n{shelves_str}"

    def __repr__(self) -> str:
        return str(self)


class Hall(BooksMixin):
    """Зал"""

    _place_to_put_attr = "_racks"
    _rack_limit = 10

    def __init__(self):
        self._racks = [Rack() for _ in range(Hall._rack_limit)]

    def __str__(self) -> str:
        racks_str = ""
        for rack in self._racks:
            if rack.get_free_space() == Rack.get_capacity():
                continue
            racks_str += f"- {rack}\n"

        return f"Зал:\n{racks_str}"

    def __repr__(self) -> str:
        return str(self)
