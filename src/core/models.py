from django.db import models

from core.base_models import BaseModel
from core.factories import HallFactory


class Library(BaseModel):
    class Meta:
        verbose_name = "библиотека"
        verbose_name_plural = "библиотеки"

    def get_available_shelf(self) -> "Shelf":
        available_shelf = None
        for hall in self.halls:
            for rack in hall.racks:
                for shelf in rack.shelves:
                    if shelf.is_available:
                        available_shelf = shelf

        if not available_shelf:
            hall = HallFactory.create(self)
            available_shelf = hall.racks.first().shelves.first()

        return available_shelf


class Hall(BaseModel):
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="halls", verbose_name="библиотека")

    class Meta:
        verbose_name = "зал"
        verbose_name_plural = "залы"


class Rack(BaseModel):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name="racks", verbose_name="зал")

    class Meta:
        verbose_name = "стеллаж"
        verbose_name_plural = "стеллажи"


class Shelf(BaseModel):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, related_name="shelves", verbose_name="стеллаж")
    limit = models.PositiveSmallIntegerField(verbose_name="лимит книг", default=10)

    class Meta:
        verbose_name = "полка"
        verbose_name_plural = "полки"

    @property
    def is_available(self):
        return self.books.count() < self.limit


class Archive(BaseModel):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "архив"
        verbose_name_plural = "архивы"


class Book(BaseModel):
    title = models.CharField(verbose_name="название")
    authors = models.TextField(verbose_name="авторы")
    published_on_year = models.PositiveSmallIntegerField(verbose_name="год издания")
    shelf = models.ForeignKey(Shelf, on_delete=models.SET_NULL, related_name="books", verbose_name="полка", null=True)
    archive = models.ForeignKey(Archive, on_delete=models.SET_NULL, related_name="books", null=True)

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
