from uuid import uuid4

import pytest

from library.models import Book


@pytest.fixture
def default_book():
    def _inner(year: int = 2025):
        return Book("Test", str(uuid4()), "Test", year)

    return _inner
