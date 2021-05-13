from .models import Level, Space


def get_available_motorcycle_spaces(level: Level) -> int:
    filled_motorcycle = level.spaces.filter(
        variety=Space.VarietyChoices.CAR,
        filled=True,
    ).count()

    return level.motorcycle_spaces - filled_motorcycle


def get_available_car_spaces(level: Level) -> int:
    filled_car = level.spaces.filter(
        variety=Space.VarietyChoices.CAR,
        filled=True,
    ).count()

    return level.car_spaces - filled_car
