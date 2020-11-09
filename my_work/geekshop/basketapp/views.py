from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import Basket


def index(request):  # чтобы не ломалось
    links_menu = [
        {'href': 'main:index', 'name': 'ГЛАВНАЯ'},
        {'href': 'main:product', 'name': 'КАТАЛОГ'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]

    context = {
        'page_title': 'корзина',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def add_book(request, pk_book):
    # basket_item = Basket.objects.filter(
    #     user=request.user,
    #     book_id=pk_book
    # ).first()
    # if not basket_item:
    #     basket_item = Basket.objects.create(
    #         user=request.user,
    #         book_id=pk_book
    #     )

    basket_item, _ = Basket.objects.get_or_create(
        user=request.user,
        book_id=pk_book
    )

    basket_item.counter += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
