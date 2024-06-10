from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True, help_text='Номер телефона какого-то формата')

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2', )


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=(forms.TextInput(attrs={'class': 'form-input'})))
    password = forms.CharField(label="Пароль", widget=(forms.PasswordInput(attrs={'class': 'form-input'})))
