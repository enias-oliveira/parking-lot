from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Level, Pricing

from .permissions import IsAdmin

from .serializers import (
    LevelsRequestSerializer,
    LevelsResponseSerializer,
    PricingSerializer,
)


class LevelsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]

    def get(self, request):

        serialized_levels = LevelsResponseSerializer(
            Level.get_all_levels(),
            many=True,
        )

        return Response(serialized_levels.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_request = LevelsRequestSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        level = Level.objects.create(**serialized_request.data)

        serialized_level = LevelsResponseSerializer(level)

        return Response(serialized_level.data, status=status.HTTP_201_CREATED)


class PricingView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]

    def post(self, request):
        serialized_request = PricingSerializer(data=request.data)

        if not serialized_request.is_valid():
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        pricing = Pricing.objects.create(**serialized_request.data)

        serialized_pricing = PricingSerializer(pricing)

        return Response(serialized_pricing.data, status=status.HTTP_201_CREATED)
