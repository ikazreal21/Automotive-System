from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("reservation/", views.Reservation, name="reservation"),
    path("about/", views.About, name="about"),
    path("contacts/", views.Contact, name="contacts"),
    path("schedule/", views.Schedule, name="schedule"),
    path("parts-and-accessories/", views.PartsAccess, name="parts"),
    path("services/", views.Services, name="services"),
    path("carwash/", views.Carwash, name="carwash"),
    # AUTH
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
