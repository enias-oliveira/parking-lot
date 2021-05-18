from django.urls import path
from .views import VehicleView, VehicleExitView

urlpatterns = [
    path("vehicles/", VehicleView.as_view()),
    path("vehicles/<int:vehicle_id>/", VehicleExitView.as_view()),
]
