from django.test import TestCase
from rest_framework.test import APIClient


class TestAccountView(TestCase):
    def setUp(self):
        self.admin_data = {
            "username": "admin",
            "password": "1234",
            "is_superuser": True,
            "is_staff": True,
        }

        self.client = APIClient()

    def test_create_admin_account(self):
        expected_account_creation_response = {
            "id": 1,
            "username": "admin",
            "is_superuser": True,
            "is_staff": True,
        }

        actual_account_creation_response = self.client.post(
            "/api/accounts/",
            self.admin_data,
            format="json",
        ).json()

        self.assertDictEqual(
            actual_account_creation_response,
            expected_account_creation_response,
        )

    def test_create_duplicated_account(self):
        self.client.post(
            "/api/accounts/",
            self.admin_data,
            format="json",
        ).json()

        duplicate_account_creation_response = self.client.post(
            "/api/accounts/",
            self.admin_data,
            format="json",
        )

        self.assertTrue(duplicate_account_creation_response.status_code, 409)

    def test_login_user(self):
        self.client.post(
            "/api/accounts/",
            self.admin_data,
            format="json",
        ).json()

        login_response = self.client.post(
            "/api/login/",
            {
                "username": self.admin_data["username"],
                "password": self.admin_data["password"],
            },
            format="json",
        )

        self.assertIn("token", login_response.json().keys())

    def test_login_inexisting_user(self):
        login_response = self.client.post(
            "/api/login/",
            {"username": "alala", "password": "ofdjsf"},
            format="json",
        )

        self.assertEqual(login_response.status_code, 401)
