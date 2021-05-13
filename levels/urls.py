from django.urls import path
from .views import LevelsView

urlpatterns = [path("levels/", LevelsView.as_view())]
