from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.

users = ['user1','trenbolonovich']
def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            info = {}
            context = {
                'info': info,
                'form': form
            }
            if username in users:
                info.update({'error': 'Такой пользователь уже существует'})
                return render(request, 'registration_page.html', context)
            if password != repeat_password:
                info.update({'error': 'Пароли не совпадают'})
                return render(request, 'registration_page.html', context)
            if int(age) < 18:
                info.update({'error': 'Вы должны быть старше 18'})
                return render(request, 'registration_page.html', context)
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}')
    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        info = {}
        context = {
            'info': info
        }
        if username in users:
            info.update({'error': 'Такой пользователь уже существует'})
            return render(request, 'registration_page.html', context)
        if password != repeat_password:
            info.update({'error': 'Пароли не совпадают'})
            return render(request, 'registration_page.html', context)
        if int(age) < 18:
            info.update({'error': 'Вы должны быть старше 18'})
            return render(request, 'registration_page.html', context)
        users.append(username)
        return HttpResponse(f'Приветствуем, {username}')

    return render(request, 'registration_page.html')