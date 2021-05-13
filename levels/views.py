from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Level

from .serializers import LevelsRequestSerializer, LevelsResponseSerializer


class LevelsView(APIView):
    # TODO Procted view so that only admins can create levels

    def get(self, request):
        return Response({"msg": "Hello Levels!"})

    def post(self, request):
        serialized_request = LevelsRequestSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        level = Level.objects.create(**serialized_request.data)

        serialized_level = LevelsResponseSerializer(level)

        return Response(serialized_level.data, status=status.HTTP_201_CREATED)
