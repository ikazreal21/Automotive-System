from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("reservation/", views.Reservation, name="reservation"),
]
