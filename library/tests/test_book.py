from library.models import Book


def test_unique_book_index():
    books = [Book("test", "test") for _ in range(5)]
    book_indices = [book.index for book in books]
    assert book_indices == list(set(book_indices))
