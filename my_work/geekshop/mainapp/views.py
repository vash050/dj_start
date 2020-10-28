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
    context = {
        'page_title': 'контакты',
    }
    return render(request, 'mainapp/contact.html', context=context)
