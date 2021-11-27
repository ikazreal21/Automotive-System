from django.db import models
from django.contrib.auth.models import User


class PartsAndAccess(models.Model):
    parts_name = models.CharField(max_length=255)
    parts_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.parts_name} {self.parts_price}"


class Services(models.Model):
    serve_name = models.CharField(max_length=255)
    serve_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.serve_name} {self.serve_price}"


class ReservationShed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    services = models.ManyToManyField(Services)
    schedule = models.DateTimeField()

    def __str__(self):
        return f"{self.user}"


class PartsOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parts = models.ManyToManyField(PartsAndAccess)

    def __str__(self):
        return f"{self.user}"
