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
    filled = models.BooleanField()

    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        related_name="spaces",
    )
