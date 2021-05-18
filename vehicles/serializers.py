from rest_framework import serializers

from .models import Vehicle

from levels.models import Space
from levels.serializers import SpaceSerializer


class VehicleRequestSerializer(serializers.Serializer):
    vehicle_type = serializers.CharField(max_length=255)
    license_plate = serializers.CharField(max_length=255)

    def validate_vehicle_type(self, value):
        vehicle_type_choices = {
            "car": Space.VarietyChoices.CAR,
            "motorcycle": Space.VarietyChoices.MOTORCYCLE,
        }

        if value not in vehicle_type_choices.keys():
            raise serializers.ValidationError()

        return vehicle_type_choices[value].value


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = serializers.SerializerMethodField()
    space = SpaceSerializer()

    class Meta:
        model = Vehicle
        fields = "__all__"
        read_only_fields = (
            "id",
            "arrived_at",
            "paid_at",
            "amount_paid",
            "space",
        )

    def get_vehicle_type(self, obj: Vehicle):
        vehicle_type_choices = {
            Space.VarietyChoices.CAR.value: "car",
            Space.VarietyChoices.MOTORCYCLE.value: "motorcylce",
        }

        return vehicle_type_choices[obj.vehicle_type]
