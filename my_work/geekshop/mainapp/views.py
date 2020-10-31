from django.shortcuts import render

from mainapp.models import GenreBooks


def get_catalog_menu():
    return GenreBooks.objects.all()


def index(request):
    links_menu = [
        {'href': 'main:index', 'name': 'ГЛАВНАЯ'},
        {'href': 'main:product', 'name': 'КАТАЛОГ'},
        # {'href': '#', 'main:name': 'ЛИЧНЫЙ КАБИНЕТ'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]
    context = {
        'page_title': 'главная',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def product(request):
    links_menu = [
        {'href': 'main:index', 'name': 'ГЛАВНАЯ'},
        {'href': 'main:product', 'name': 'КАТАЛОГ'},
        # {'href': '#', 'main:name': 'ЛИЧНЫЙ КАБИНЕТ'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]
    context = {
        'page_title': 'каталог',
        'links_menu': links_menu,
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/product.html', context=context)


def contact(request):
    links_menu = [
        {'href': 'main:index', 'name': 'ГЛАВНАЯ'},
        {'href': 'main:product', 'name': 'КАТАЛОГ'},
        # {'href': '#', 'main:name': 'ЛИЧНЫЙ КАБИНЕТ'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]
    locations = [
        {
            'city': 'Москва',
            'phone': '8(954) 145-45-85',
            'mail': 'moskow@bookshoop.ru',
            'address': 'ул. Ленина 45',
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '8(812)121-21-21',
            'mail': 'spb@bookshoop.ru',
            'address': 'пр. Невский 12',
        },
        {
            'city': 'Барнаул',
            'phone': '8(365) 194-34-12',
            'mail': 'barnaul@bookshoop.ru',
            'address': 'ул. Тракторная 18',
        },
    ]
    context = {
        'page_title': 'контакты',
        'locations': locations,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/contact.html', context=context)


def product_deails(request):
    links_menu = [
        {'href': 'main:index', 'name': 'ГЛАВНАЯ'},
        {'href': 'main:product', 'name': 'КАТАЛОГ'},
        # {'href': '#', 'main:name': 'ЛИЧНЫЙ КАБИНЕТ'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]
    context = {
        'page_title': 'товар',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/product_deails.html', context=context)
