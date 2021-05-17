from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class VehicleView(APIView):
    def get(self, request):
        return Response({"msg": "Hello Vechicles"}, status=status.HTTP_200_OK)
