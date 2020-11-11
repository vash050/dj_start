from django.urls import path

import basketapp.views as basketapp


app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add_book/<int:book_pk>/', basketapp.add_book, name='add_book'),
    path('remove_book/<int:basket_pk>/', basketapp.remove_book, name='remove_book'),
]
