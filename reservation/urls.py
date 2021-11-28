from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("reservation/", views.Reservation, name="reservation"),
    # AUTH
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
