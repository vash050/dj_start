from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def product(request):
    return render(request, 'mainapp/product.html')

def contact(request):
    return render(request, 'mainapp/contact.html')
