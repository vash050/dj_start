import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from mainapp.models import GenreBooks, Book


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
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

        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
