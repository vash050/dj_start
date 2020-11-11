from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

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
def add_book(request, book_pk):
    basket_item = request.user.basket.filter(
        book_id=book_pk
    ).first()
    if not basket_item:
        basket_item = Basket.objects.create(
            user=request.user,
            book_id=book_pk
        )

    basket_item.counter += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_book(request, basket_pk):
    basket_item = get_object_or_404(Basket, book_id=basket_pk)
    basket_item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
