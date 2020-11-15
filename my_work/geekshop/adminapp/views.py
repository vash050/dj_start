from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    users = get_user_model().objects.all()
    context = {
        'page_title': 'админка/пользователи',
        'object_list': users,
    }
    return render(request, 'myadminapp/index.html', context=context)
