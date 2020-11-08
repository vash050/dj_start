from django.http import HttpResponseRedirect

from basketapp.models import Basket


def index(request):
    pass


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
