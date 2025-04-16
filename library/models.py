class Book:
    """Книга"""

    _book_index = 0

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.index = Book._book_index
        Book._book_index += 1

    def __str__(self) -> str:
        return f"{self.title}, {self.author}, №{self.index}"

    def __repr__(self) -> str:
        return str(self)


class Shelf:
    """Полка"""

    def __init__(self, *books: list[Book] | None):
        if len(books) > 10:
            raise ValueError("На полке не может храниться больше 10 книг")
        self.books = list(books)

    def add_books(self, *books: list[Book] | None):
        """Добавление книг

        :param books: Книги
        :return:
        """
        if len(books) + len(self.books) > 10:
            raise ValueError("На полке не может храниться больше 10 книг")
        self.books.extend(books)

    def __str__(self) -> str:
        books_str = "; ".join(str(book) for book in self.books)
        return f"Полка с книгами: {books_str}"

    def __repr__(self) -> str:
        return str(self)
