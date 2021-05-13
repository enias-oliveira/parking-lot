from django.test import TestCase
from rest_framework.test import APIClient


class TestLevelView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.level_data = {
            "name": "floor 1",
            "fill_priority": 2,
            "motorcycle_spaces": 1,
            "car_spaces": 2,
        }

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

    def test_create_level(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.admin_token)

        level_response = self.client.post(
            "/api/levels/",
            self.level_data,
            format="json",
        )

        expected = {
            "id": 1,
            "name": "floor 1",
            "fill_priority": 2,
            "available_spaces": {
                "available_motorcycle_spaces": 1,
                "available_car_spaces": 2,
            },
        }

        self.assertDictEqual(level_response.json(), expected)

    def test_create_level_not_admin(self):
        not_admin_user = {
            "username": "not-admin",
            "password": "1234",
            "is_superuser": False,
            "is_staff": True,
        }

        not_admin_login = {
            "username": "not-admin",
            "password": "1234",
        }

        self.client.post("/api/accounts/", not_admin_user, format="json")

        not_admin_token = self.client.post(
            "/api/login/",
            not_admin_login,
            format="json",
        ).json()["token"]

        self.client.credentials(HTTP_AUTHORIZATION="Token " + not_admin_token)

        level_response = self.client.post(
            "/api/levels/", self.level_data, format="json"
        )

        self.assertEqual(level_response.status_code, 401)
