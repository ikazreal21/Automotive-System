from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import *


class DateInput(forms.DateInput):
    input_type = "date"


class ReservationForm(forms.ModelForm):
    class Meta:
        model = ReservationShed
        fields = "__all__"

        widgets = {"schedule": DateInput(), "services": forms.CheckboxSelectMultiple}


class PartsOrderForm(forms.ModelForm):
    class Meta:
        model = PartsOrder
        fields = ["parts"]

        widgets = {"parts": forms.CheckboxSelectMultiple}


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
