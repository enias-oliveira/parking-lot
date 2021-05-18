from .models import Level, Space


def get_all_levels() -> list[Level]:
    return Level.objects.all()


def get_available_motorcycle_spaces(level: Level) -> int:
    filled_motorcycle = level.spaces.filter(
        variety=Space.VarietyChoices.MOTORCYCLE,
    ).count()

    return level.motorcycle_spaces - filled_motorcycle


def get_available_car_spaces(level: Level) -> int:
    filled_car = level.spaces.filter(
        variety=Space.VarietyChoices.CAR,
    ).count()

    return level.car_spaces - filled_car
