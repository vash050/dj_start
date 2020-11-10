from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from basketapp.models import Basket


@login_required
def index(request):
    basket = request.user.basket.all()

    context = {
        'page_title': 'корзина',
        'basket': basket,
    }
    return render(request, 'basketapp/index.html', context=context)


@login_required
def add_book(request, pk_book):
    basket_item = request.user.basket.filter(
        book_id=pk_book
    ).first()
    if not basket_item:
        basket_item = Basket.objects.create(
            user=request.user,
            book_id=pk_book
        )

    basket_item.counter += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
