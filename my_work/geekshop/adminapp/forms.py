from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import forms, HiddenInput, ModelForm

from mainapp.models import GenreBooks, Book


class AgeValidationMixin:
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('вы слишком молоды!')
        return age


class AdminShopUserCreateForm(UserCreationForm, AgeValidationMixin):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2',
                  'email', 'age', 'avatar', 'is_staff', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


class AdminShopUserUpdateForm(UserChangeForm, AgeValidationMixin):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password', 'email',
                  'age', 'avatar', 'is_staff', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            field.help_text = ''
            if field_name == 'password':
                field.widget = HiddenInput()


class AdminProductCategoryUpdateForm(ModelForm):
    class Meta:
        model = GenreBooks
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class AdminProductUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            if field_name == 'category':
                field.widget = HiddenInput()
