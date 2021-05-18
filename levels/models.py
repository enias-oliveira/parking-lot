from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=255)
    fill_priority = models.IntegerField()
    motorcycle_spaces = models.IntegerField()
    car_spaces = models.IntegerField()

    @staticmethod
    def get_all_levels():
        return Level.objects.all()

    def get_available_motorcycle_spaces(self) -> int:
        filled_motorcycle = self.spaces.filter(
            variety=Space.VarietyChoices.MOTORCYCLE,
        ).count()

        return self.motorcycle_spaces - filled_motorcycle

    def get_available_car_spaces(self) -> int:
        filled_car = self.spaces.filter(
            variety=Space.VarietyChoices.CAR,
        ).count()

        return self.car_spaces - filled_car

    def has_available_spaces(self, variety: str):
        if variety == Space.VarietyChoices.MOTORCYCLE.value:
            return self.get_available_motorcycle_spaces() > 0
        else:
            return self.get_available_car_spaces() > 0


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
