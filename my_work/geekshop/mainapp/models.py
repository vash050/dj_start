from django.db import models


class GenreBooks(models.Model):
    genre = models.CharField('жанр книги', max_length=64)
    description = models.TextField('Описание жанра', blank=True)

    class Meta:
        verbose_name = 'жанр книг'
        verbose_name_plural = 'жанры книг'
        ordering = ['genre']

    def __str__(self):
        return f'{self.genre}'


class Book(models.Model):
    genre_book = models.ForeignKey(GenreBooks, on_delete=models.CASCADE)
    name = models.CharField('книга', max_length=64)
    image = models.ImageField(upload_to='books_images', blank=True)
    author = models.CharField('автор', max_length=64)
    description = models.TextField('Описание', blank=True)
    short_description = models.CharField('краткое описание', max_length=64, blank=True)
    price = models.DecimalField('цена', max_digits=7, decimal_places=2, default=0)
    count_page = models.PositiveSmallIntegerField('количество страниц', default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.name} ({self.genre_book})'


