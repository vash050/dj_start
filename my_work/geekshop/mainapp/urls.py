from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('product/', mainapp.product, name='product'),
    path('contact/', mainapp.contact, name='contact'),
    path('product_details/', mainapp.product_details, name='product_details'),
    path('catalog_page/<int:genre_pk>/', mainapp.catalog_page, name='catalog_page'),
]
