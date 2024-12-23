from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class Platform(TemplateView):
    template_name = 'platform.html'


def Games(request):
    title = 'Игрулечки'
    games = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    context = {
        'title': title,
        'games': games,
    }
    return render(request, 'games.html', context, )


def Cart(request):
    title = 'Корзина'
    cart = []
    cart_len=len(cart)
    context = {
        'title': title,
        'cart': cart,
        'cart_len': cart_len,
    }
    return render(request, 'cart.html', context)


