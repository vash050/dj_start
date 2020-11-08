from django.contrib.auth import get_user_model
from django.db import models

from mainapp.models import Book


class Basket(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    counter = models.IntegerField('количество', default=0)
    add_datetime = models.DateTimeField('время', auto_now_add=True)
