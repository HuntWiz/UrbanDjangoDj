from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class Platform(TemplateView):
    template_name = 'platform.html'


def Games(request):
    title = 'Игры'
    context = {
        'title': title
    }
    return render(request,'games.html', context )

def Cart(request):
    title = 'Корзина пуста'
    context = {
        'title': title
    }
    return render(request, 'cart.html', context)