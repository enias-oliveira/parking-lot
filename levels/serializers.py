from rest_framework import serializers

from .models import Level, Pricing

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
