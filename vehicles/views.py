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

        try:
            levels_with_spaces = [
                level
                for level in Level.objects.order_by("fill_priority")
                if level.has_available_spaces(
                    serialized_request.data["vehicle_type"],
                )
            ]

            level_with_spaces = levels_with_spaces[0]

            space = Space.objects.create(
                variety=serialized_request.data["vehicle_type"],
                level=level_with_spaces,
            )

            vehicle = Vehicle.objects.create(**serialized_request.data, space=space)

            serialized_vehicle = VehicleSerializer(vehicle)

            return Response(serialized_vehicle.data, status=status.HTTP_201_CREATED)

        except IndexError:
            return Response(
                {"msg": "No Levels or Spaces available"},
                status=status.HTTP_404_NOT_FOUND,
            )
