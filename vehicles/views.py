from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VehicleSerializer, VehicleRequestSerializer

from .models import Vehicle

from levels.models import Level, Space


class VehicleView(APIView):
    def post(self, request):
        serialized_request = VehicleRequestSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        level = Level.objects.order_by("fill_priority")[0]

        space = Space.objects.create(
            variety=serialized_request.data["vehicle_type"],
            level=level,
        )

        vehicle = Vehicle.objects.create(**serialized_request.data, space=space)

        serialized_vehicle = VehicleSerializer(vehicle)

        return Response(serialized_vehicle.data, status=status.HTTP_201_CREATED)
