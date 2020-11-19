from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('', adminapp.index, name='index'),
    path('', adminapp.ShopUserList.as_view(), name='index'),
    # path('user/create/', adminapp.user_create, name='user_create'),
    path('user/create/', adminapp.ShopUseCreateView.as_view(), name='user_create'),
    # path('user/update/<int:user_pk>/', adminapp.user_update, name='user_update'),
    path('user/update/<int:pk>/', adminapp.ShopUserUpdateView.as_view(), name='user_update'),
    # path('user/delete/<int:user_pk>/', adminapp.user_delete, name='user_delete'),
    path('user/delete/<int:pk>/', adminapp.ShopUserDeleteView.as_view(), name='user_delete'),

    path('categories/', adminapp.categories, name='categories'),
]
