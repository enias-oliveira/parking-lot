from django.urls import path
from .views import LevelsView, PricingView

urlpatterns = [
    path("levels/", LevelsView.as_view()),
    path("pricings/", PricingView.as_view()),
]
