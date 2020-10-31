from django.db import models


class GenreBooks(models.Model):
    genre = models.CharField('жанр книги', max_length=64)
    description = models.TextField('Описание жанра', blank=True)


class Book(models.Model):
    genre_book = models.ForeignKey(GenreBooks, on_delete=models.CASCADE)
    name = models.CharField('книга', max_length=64)
    author = models.CharField('автор', max_length=64)
    description = models.TextField('Описание', blank=True)
    short_description = models.CharField('краткое описание', max_length=64, blank=True)
    price = models.DecimalField('цена', max_digits=7, decimal_places=2, default=0)
    count_page = models.PositiveSmallIntegerField('количество страниц', default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)


