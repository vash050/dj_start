from django.urls import path

import basketapp.views as basketapp


app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.index, name='index'),
    path('add_book/<int:pk_book>/', basketapp.add_book, name='add_book'),
]
