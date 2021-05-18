from rest_framework import serializers

from .models import Level, Pricing, Space

from .services import get_available_car_spaces, get_available_motorcycle_spaces


class LevelsRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    fill_priority = serializers.IntegerField()
    motorcycle_spaces = serializers.IntegerField()
    car_spaces = serializers.IntegerField()


class LevelsResponseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    fill_priority = serializers.IntegerField()
    available_spaces = serializers.SerializerMethodField()

    class Meta:
        model = Level
        fields = ["id", "name", "fill_priority", "available_spaces"]

    def get_available_spaces(self, obj):
        return {
            "available_motorcycle_spaces": get_available_motorcycle_spaces(obj),
            "available_car_spaces": get_available_car_spaces(obj),
        }


class PricingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pricing
        fields = ["id", "a_coefficient", "b_coefficient"]


class SpaceSerializer(serializers.ModelSerializer):
    variety = serializers.SerializerMethodField()
    level_name = serializers.SerializerMethodField()

    class Meta:
        model = Space
        fields = ["id", "variety", "level_name"]
        read_only_fields = ("id",)

    def get_variety(self, obj: Space):
        variety_choices = {
            Space.VarietyChoices.CAR.value: "car",
            Space.VarietyChoices.MOTORCYCLE.value: "motorcylce",
        }

        return variety_choices[obj.variety]

    def get_level_name(self, obj: Space):
        return obj.level.name
