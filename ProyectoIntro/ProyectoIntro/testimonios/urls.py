from django.urls import include, path
from . import views
urlpatterns= [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("subirtesti/", views.subirtesti, name="subirtesti"),
    path("vertesti/", views.vertesti, name="vertesti"),

    path('revisartesti/<int:pk>/', views.revisartesti, name="revisartesti"),

]
