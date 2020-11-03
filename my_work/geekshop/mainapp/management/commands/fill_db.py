import json

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from mainapp.models import GenreBook, Book


def load_from_json(file_name):
    with open(file_name, encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    # help = 'Fill data in database'
    #
    # def handle(self, *args, **options):
    #     items = load_from_json('')  # путь к файлу
    #     for item in items:
    #         GenreBook.objects.create(**item)
    #
    #     items = load_from_json('')  # путь к файлу
    #     for item in items:
    #         genre = GenreBook.objects.get(name=item[''])
    #         item[''] = genre
    #         Book.objects.create(**item)

    if not User.objects.filter(username='django').exists():
        User.objects.create_superuser('django', 'django@gb.local', 'geekbrains')
