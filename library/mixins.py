class AddBooksMixin:
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
