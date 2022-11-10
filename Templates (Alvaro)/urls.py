from django.urls import path
from . import views

urlpatterns = [
        path('home/',views.home),
        path('foro/',views.foro),
        path('test/',views.test),
        path('faq/',views.faq),
        path('about/',views.about)

]