class AddBooksMixin:
    """
    Миксин для функционала добавления книг в сущность, которая предполагает добавление книг во вложенные сущности

    Для работы миксина необходимо у класса указать параметр _place_to_put_attr: str,
    обозначающий список вложенных сущностей класса.
    Также необходимо, чтобы у вложенной сущности были реализованы методы get_free_space и add_books.
    """

    def add_books(self, *books: tuple):
        """Добавление книг

        :param books: Книги
        :return:
        """
        free_space = self.get_free_space()
        if len(books) > free_space:
            raise ValueError("Закончилось место для книг")

        offset = 0
        added_books_count = 0
        while added_books_count < len(books):
            for place_to_put in getattr(self, self._place_to_put_attr):
                free_space = place_to_put.get_free_space()
                place_to_put.add_books(*books[offset : offset + free_space])
                offset += free_space
                added_books_count += free_space

    def get_free_space(self) -> int:
        """Узнать, сколько места осталось

        :return: Кол-во свободных мест
        """
        free_space = 0
        for place_to_put in getattr(self, self._place_to_put_attr):
            free_space += place_to_put.get_free_space()

        return free_space


class GetBooksMixin:
    def get_books(self):
        books = []
        for place_to_put in getattr(self, self._place_to_put_attr):
            books.extend(place_to_put.get_books())

        return books


class DeleteBooksMixin:
    def remove_book(self, book):
        for place_to_put in getattr(self, self._place_to_put_attr):
            if book in place_to_put.get_books():
                place_to_put.remove_book(book)
                break


class BooksMixin(AddBooksMixin, GetBooksMixin, DeleteBooksMixin):
    pass
