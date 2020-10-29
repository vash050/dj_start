from django.shortcuts import render


def index(request):
    context = {
        'page_title': 'главная',
    }
    return render(request, 'mainapp/index.html', context=context)


def product(request):
    context = {
        'page_title': 'каталог',
    }
    return render(request, 'mainapp/product.html', context=context)


def contact(request):
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
    }
    return render(request, 'mainapp/contact.html', context=context)
