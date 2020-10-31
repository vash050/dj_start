from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),
    path('product/', mainapp.product, name='product'),
    path('contact/', mainapp.contact, name='contact'),
    path('product_deails/', mainapp.product_deails, name='product_deails'),
]
