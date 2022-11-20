"""ProyectoIntro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin

from ProyectoIntro.views import hola_mundo, mapas
from ProyectoIntro.views import despedida
from ProyectoIntro.views import mapas
from ProyectoIntro.views import casa
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.urls import path, include
from register import views as v
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("holamundo/", hola_mundo),
    path("despedida/", despedida),
    path("mapa/", mapas),
    path("ini/", casa),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", v.register, name="register"),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('home/',views.home),
    path('foro/',views.foro),
    path('test/',views.test),
    path('faq/',views.faq),
    path('about/',views.about),
    path("testimonios/", include('testimonios.urls')),
    ]
