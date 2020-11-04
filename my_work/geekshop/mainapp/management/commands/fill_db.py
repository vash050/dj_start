import json

from django.core.management.base import BaseCommand, CommandError

from mainapp.models import GenreBooks, Book

from authapp.models import ShopUser


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    """
    таблицы связаны по id, но это потому что для получения json я парсил бд проекта,
    в реальности я бы использовал для связи наименования жанра
    """
    help = 'Fill data in database'

    def handle(self, *args, **options):
        items = load_from_json('mainapp/json/genre.json')  # путь к файлу
        for item in items:
            GenreBooks.objects.create(**item)

        items = load_from_json('mainapp/json/book.json')  # путь к файлу
        for item in items:
            genre = GenreBooks.objects.get(id=item['genre_book'])
            item['genre_book'] = genre
            Book.objects.create(**item)

        if not ShopUser.objects.filter(username='django').exists():
            ShopUser.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
