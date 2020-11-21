from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.ShopUserList.as_view(), name='index'),
    path('user/create/', adminapp.ShopUseCreateView.as_view(), name='user_create'),
    path('user/update/<int:pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/', adminapp.categories, name='categories'),
    path('categories/create/', adminapp.GenreBooksCreateView.as_view(), name='categories_create'),
    path('categories/update/<int:pk>/', adminapp.GenreBooksUpdateView.as_view(), name='categories_update'),
    path('categories/delete/<int:pk>/', adminapp.GenreBooksDeleteView.as_view(), name='categories_delete'),
    path('categories/<int:pk>/products/', adminapp.category_products, name='category_products'),
    path('product/<int:pk>/', adminapp.ProductDetail.as_view(), name='product_detail'),
    path('categories/<int:pk>/product/create/', adminapp.product_create, name='product_create'),
]
