from django.urls import path
from . import views

urlpatterns = [
        path('',views.home),
        path('home/',views.home),
        path('testimonio/',views.testimonio),
        path('test/',views.test),
        path('faq/',views.faq),
        path('about/',views.about),
        path('ansiedad/',views.ansiedad),
        path('burnout/',views.ansiedad),
        path('depresion/',views.ansiedad),

]