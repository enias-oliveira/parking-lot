from django.test import TestCase
from rest_framework.test import APIClient

from datetime import datetime


class TestVehicleView(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.admin_data = {
            "username": "admin",
            "password": "1234",
            "is_superuser": True,
            "is_staff": True,
        }

        self.admin_login = {
            "username": "admin",
            "password": "1234",
        }

        self.client.post("/api/accounts/", self.admin_data, format="json")

        self.admin_token = self.client.post(
            "/api/login/", self.admin_login, format="json"
        ).json()["token"]

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token)

        self.level_1_data = {
            "name": "floor 1",
            "fill_priority": 1,
            "motorcycle_spaces": 2,
            "car_spaces": 4,
        }

        self.level_2_data = {
            "name": "floor 2",
            "fill_priority": 2,
            "motorcycle_spaces": 1,
            "car_spaces": 2,
        }

        self.levels_route = "/api/levels/"

        self.client.post(
            self.levels_route,
            self.level_1_data,
            format="json",
        )

        self.client.post(
            self.levels_route,
            self.level_2_data,
            format="json",
        )

        self.pricing_data = {"a_coefficient": 100, "b_coefficient": 100}

        self.pricings_route = "/api/pricings/"

        self.client.post(self.pricings_route, self.pricing_data, format="json")

        self.vehicles_route = "/api/vehicles/"

    def test_standard_vehicle_registration(self):
        expected_json_response = {
            "id": 1,
            "license_plate": "AYO1029",
            "vehicle_type": "car",
            "paid_at": None,
            "amount_paid": None,
            "space": {"id": 1, "variety": "car", "level_name": "floor 1"},
        }

        expected_level_1 = {
            "id": 1,
            "name": "floor 1",
            "fill_priority": 1,
            "available_spaces": {
                "available_motorcycle_spaces": 2,
                "available_car_spaces": 3,
            },
        }

        vehicle_data = {"vehicle_type": "car", "license_plate": "AYO1029"}

        actual_response = self.client.post(
            self.vehicles_route,
            vehicle_data,
            format="json",
        )

        self.assertDictContainsSubset(expected_json_response, actual_response.json())

        levels = self.client.get(self.levels_route).json()
        actual_level_1 = levels[0]

        self.assertEqual(actual_level_1, expected_level_1)
