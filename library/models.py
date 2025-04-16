class Book:
    """
    Класс книги
    """

    _book_index = 0

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.index = Book._book_index
        Book._book_index += 1

    def __str__(self):
        return f"{self.title}, {self.author}, №{self.index}"

    def __repr__(self):
        return str(self)
