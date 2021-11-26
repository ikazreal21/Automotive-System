from django.shortcuts import render


def Home(request):
    return render(request, "reservation/home.html")


def Reservation(request):
    return render(request, "")
