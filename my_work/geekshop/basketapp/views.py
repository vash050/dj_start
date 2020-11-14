from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from django.template import loader


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


@login_required
def update_book(request, basket_pk, qty):
    if request.is_ajax():
        basket_item = Basket.objects.filter(pk=basket_pk).first()
        if not basket_item:
            return JsonResponse(
                {'status': 'error'},
                status_code=404
            )
        if qty <= 0:
            basket_item.delete()
        else:
            basket_item.counter += qty
            basket_item.save()

        basket = request.user.basket.all()
        context = {
            'basket': basket,
        }
        basket_list = loader.render_to_string(
            'basketapp/includes/inc__basket_list.html',
            context=context,
            request=request
        )
        return JsonResponse({
            'status': 'ok',
            'basket_list': basket_list
        })
