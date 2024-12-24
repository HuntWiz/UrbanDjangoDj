from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30,label='Ваш логин')
    password = forms.CharField(min_length=8,label='Ваш пароль')
    repeat_password = forms.CharField(min_length=8,label='Повтор пароля')
    age = forms.CharField(max_length=3,label='Ваш возраст')