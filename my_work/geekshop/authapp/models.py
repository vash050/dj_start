from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    age = models.PositiveIntegerField('возраст',
                                      null=True)
    avatar = models.ImageField('аватар', upload_to='avatars', blank=True)

    def basket_total_cost(self):
        return sum(map(lambda x: x.book_cost, self.basket.all()))

    def basket_total_qty(self):
        return sum(map(lambda x: x.counter, self.basket.all()))

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()
        return 1, {}
