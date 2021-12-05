from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import *
from .models import *


def Register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account Created For " + user)
                return redirect("login")

        context = {"form": form}
    return render(request, "reservation/register.html", context)


def Login(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or Password is Incorrect")

    context = {}
    return render(request, "reservation/login.html")


def Logout(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
def Home(request):
    return render(request, "reservation/home.html")


@login_required(login_url="login")
def Reservation(request):
    reservationform = ReservationForm()
    if request.method == "POST":
        reservationform = ReservationForm(request.POST)
        if reservationform.is_valid():
            reservationform.save(commit=False).user = request.user
            reservationform.save()
        return redirect("/")
    context = {"form": reservationform}
    return render(request, "reservation/reservation.html", context)


@login_required(login_url="login")
def Schedule(request):
    reservation = ReservationShed.objects.all()
    return render(request, "reservation/sched.html", {"sched": reservation})


@login_required(login_url="login")
def PartsAccess(request):
    form = PartsOrderForm()
    if request.method == "POST":
        form = PartsOrderForm(request.POST)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save()
        return redirect("parts")
    context = {"form": form}
    return render(request, "reservation/parts-acces.html", context)


@login_required(login_url="login")
def Carwash(request):
    return render(request, "reservation/carwash.html")


@login_required(login_url="login")
def Services(request):
    return render(request, "reservation/services.html")


@login_required(login_url="login")
def About(request):
    return render(request, "reservation/about.html")


@login_required(login_url="login")
def Contact(request):
    return render(request, "reservation/contacts.html")
