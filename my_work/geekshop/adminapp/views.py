from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy

from adminapp.forms import AdminShopUserCreateForm, AdminShopUserUpdateForm
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from mainapp.models import GenreBooks, Book

from adminapp.forms import AdminProductCategoryUpdateForm, AdminProductUpdateForm


class SuperUserOnlyMixin:
    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SetPageTitleMixin:
    page_title = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['page_title'] = self.page_title
        return context


# @user_passes_test(lambda x: x.is_superuser)
# def user_create(request):
#     if request.method == 'POST':
#         user_form = AdminShopUserCreateForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:index'))
#     else:
#         user_form = AdminShopUserCreateForm()
#
#     context = {
#         'page_title': 'админка/пользователи/создание',
#         'form': user_form
#     }
#     return render(request, 'adminapp/user_update.html', context=context)


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     users = get_user_model().objects.all()
#     context = {
#         'page_title': 'админка/пользователи',
#         'object_list': users,
#     }
#     return render(request, 'adminapp/index.html', context=context)

class ShopUserList(SuperUserOnlyMixin, SetPageTitleMixin, ListView):
    model = get_user_model()
    page_title = 'админка/пользователи'


class ShopUseCreateView(SuperUserOnlyMixin, SetPageTitleMixin, CreateView):
    model = get_user_model()
    form_class = AdminShopUserCreateForm
    success_url = reverse_lazy('adminapp:index')
    page_title = 'админка/пользователи/создание'


class ShopUserUpdateView(SuperUserOnlyMixin, SetPageTitleMixin, UpdateView):
    model = get_user_model()
    form_class = AdminShopUserUpdateForm
    success_url = reverse_lazy('adminapp:index')
    page_title = 'админка/пользователи/редактирование'


class ShopUserDeleteView(SuperUserOnlyMixin, SetPageTitleMixin, DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('adminapp:index')
    page_title = 'админка/пользователи/удаление'


# @user_passes_test(lambda x: x.is_superuser)
# def user_update(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     if request.method == 'POST':
#         user_form = AdminShopUserUpdateForm(request.POST, request.FILES, instance=user)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('adminapp:index'))
#     else:
#         user_form = AdminShopUserUpdateForm(instance=user)
#
#     context = {
#         'page_title': 'админка/пользователи/редактирование',
#         'form': user_form
#     }
#     return render(request, 'adminapp/user_update.html', context=context)


# @user_passes_test(lambda x: x.is_superuser)
# def user_delete(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     if not user.is_active or request.method == 'POST':
#         if user.is_active:
#             user.is_active = False
#             user.save()
#         return HttpResponseRedirect(reverse('adminapp:index'))
#
#     context = {
#         'page_title': 'админка/пользователи/удаление',
#         'object': user
#     }
#     return render(request, 'adminapp/user_delete.html', context=context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    items = GenreBooks.objects.all()
    context = {
        'page_title': 'админка/категории',
        'object_list': items,
    }
    return render(request, 'adminapp/categories_list.html', context=context)


class GenreBooksCreateView(SuperUserOnlyMixin, SetPageTitleMixin, CreateView):
    model = GenreBooks
    form_class = AdminProductCategoryUpdateForm
    success_url = reverse_lazy('adminapp:categories')
    page_title = 'админка/категории/создание'


class GenreBooksUpdateView(SuperUserOnlyMixin, SetPageTitleMixin, UpdateView):
    model = GenreBooks
    form_class = AdminProductCategoryUpdateForm
    success_url = reverse_lazy('adminapp:categories')
    page_title = 'админка/категории/редактирование'


class GenreBooksDeleteView(SuperUserOnlyMixin, SetPageTitleMixin, DeleteView):
    model = GenreBooks
    success_url = reverse_lazy('adminapp:categories')
    page_title = 'админка/пользователи/удаление'


@user_passes_test(lambda x: x.is_superuser)
def category_products(request, pk):
    category = get_object_or_404(GenreBooks, pk=pk)
    object_list = category.book_set.all()
    context = {
        'page_title': f'категория {category.genre}/книги',
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/category_products_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    category = get_object_or_404(GenreBooks, pk=pk)
    if request.method == 'POST':
        form = AdminProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'adminapp:category_products',
                kwargs={'pk': category.pk}
            ))
    else:
        form = AdminProductUpdateForm(
            initial={
                'genre_book': category,
            }
        )
    context = {
        'page_title': 'продукты/создание',
        'form': form,
        'category': category,
    }
    return render(request, 'adminapp/product_update.html', context)


class ProductDetail(SuperUserOnlyMixin, DetailView):
    model = Book
