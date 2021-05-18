from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=255)
    fill_priority = models.IntegerField()
    motorcycle_spaces = models.IntegerField()
    car_spaces = models.IntegerField()


class Space(models.Model):
    class VarietyChoices(models.TextChoices):
        CAR = "C"
        MOTORCYCLE = "M"

    variety = models.CharField(choices=VarietyChoices.choices, max_length=1)

    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="spaces",
    )


class Pricing(models.Model):
    a_coefficient = models.IntegerField()
    b_coefficient = models.IntegerField()

    def calculate_pricing(self, hours_parked: float) -> float:
        return self.a_coefficient + (self.b_coefficient * hours_parked)
