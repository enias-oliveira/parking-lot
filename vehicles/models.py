from django.db import models

from levels.models import Space


class Vehicle(models.Model):
    license_plate = models.CharField(max_length=255)
    vehicle_type = models.CharField(
        choices=Space.VarietyChoices.choices,
        max_length=1,
    )

    arrived_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateField(null=True)
    amount_paid = models.FloatField(null=True)

    space = models.OneToOneField(
        Space,
        on_delete=models.CASCADE,
    )
