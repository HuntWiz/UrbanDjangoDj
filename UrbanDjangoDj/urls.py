"""
URL configuration for UrbanDjangoDj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UrbanDjangoDj.task2.views import Index
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Index.as_view),
    path('index2/', TemplateView.as_view(template_name='func_index.html'))
]