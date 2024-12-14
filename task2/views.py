from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


# Create your views here.

class Index(TemplateView):
    template_name = 'obj_index.html'