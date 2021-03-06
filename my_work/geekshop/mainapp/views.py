import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from mainapp.models import GenreBooks

from mainapp.models import Book


def get_catalog_menu():
    return GenreBooks.objects.all()


def get_hot_book():
    books = Book.objects.all()
    return random.choice(books)


def get_same_books(book):
    return Book.objects.filter(genre_book=book.genre_book).exclude(pk=book.pk)


def index(request):
    links_menu = [
        {'href': 'main:index', 'name': 'главная'},
        {'href': 'main:product', 'name': 'каталог'},
        {'href': 'main:contact', 'name': 'КОНТАКТЫ'},
    ]
    context = {
        'page_title': 'главная',
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/index.html', context=context)


def product(request):
    hot_book = get_hot_book()
    links_menu = [
        {'href': 'main:index', 'name': 'главная'},
        {'href': 'main:product', 'name': 'каталог'},
        {'href': 'main:contact', 'name': 'контакты'},
    ]
    context = {
        'page_title': 'каталог',
        'same_books': get_same_books(hot_book),
        'hot_book': hot_book,
        'links_menu': links_menu,
        'catalog_menu': get_catalog_menu(),
    }
    return render(request, 'mainapp/product.html', context=context)


def contact(request):
    links_menu = [
        {'href': 'main:index', 'name': 'главная'},
        {'href': 'main:product', 'name': 'каталог'},
        {'href': 'main:contact', 'name': 'контакты'},
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


def catalog_page(request, genre_pk, page_num=1):
    if genre_pk == 0:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(genre_book_id=genre_pk)

    products_paginator = Paginator(books, 2)
    try:
        books = products_paginator.page(page_num)
    except PageNotAnInteger:
        books = products_paginator.page(1)
    except EmptyPage:
        books = products_paginator.page(products_paginator.num_pages)

    links_menu = [
        {'href': 'main:index', 'name': 'главная'},
        {'href': 'main:product', 'name': 'каталог'},
        {'href': 'main:contact', 'name': 'контакты'},
    ]

    context = {
        'page_title': 'каталог',
        'links_menu': links_menu,
        'catalog_menu': get_catalog_menu(),
        'books': books,
        'genre_pk': genre_pk,
    }
    return render(request, 'mainapp/product.html', context=context)


def product_details(request, book_pk):
    item = get_object_or_404(Book, pk=book_pk)

    links_menu = [
        {'href': 'main:index', 'name': 'главная'},
        {'href': 'main:product', 'name': 'каталог'},
        {'href': 'main:contact', 'name': 'контакты'},
    ]

    context = {
        'page_title': 'книга',
        'links_menu': links_menu,
        'catalog_menu': get_catalog_menu(),
        'item': item,
        'book_pk': item.id,
    }
    return render(request, 'mainapp/product_details.html', context=context)
