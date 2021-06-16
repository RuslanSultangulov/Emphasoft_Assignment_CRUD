from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User as AuthUser
from rest_framework.test import APITestCase
from .models import User


class AuthTokenObtainingTestCase(APITestCase):

    def setUp(self):
        self.path = reverse('api_token_auth')
        AuthUser.objects.create_user(username="correct_username",
                                     password="correct_password")

    def test_token_get_not_allowed(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_token_incorrect_credentials(self):
        data = {"username": "incorrect_username",
                "password": "incorrect_password"}
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_success(self):
        data = {"username": "correct_username",
                "password": "correct_password"}
        response = self.client.post(self.path, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UsersViewTestCase(APITestCase):
    def setUp(self):
        self.path = reverse('users_view')
        self.user = AuthUser.objects.create_user(username="correct_username",
                                                 password="correct_password")
        self.client.force_authenticate(user=self.user, token='123')

    def test_get_request(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request(self):
        data = {
            "username": "test_username",
            "first_name": "first_name",
            "last_name": "last_name",
            "password": "password",
            "is_active": True,
            "last_login": "null"
        }
        response = self.client.post(self.path, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UsersViewByIdTestCase(APITestCase):
    def setUp(self):
        self.path = reverse('user_view_by_id', kwargs={"pk": 1})
        User.objects.create(username="init_username",
                            first_name="init_first_name",
                            last_name="init_last_name",
                            password="init_password",
                            is_active=True,
                            last_login="null")
        self.user = AuthUser.objects.create_user(
            username="correct_username", password="correct_password")
        self.client.force_authenticate(user=self.user, token='123')

    def test_get_request(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_request(self):
        request_data = {
            "username": "new_test_username",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "password": "new_password",
            "is_active": False,
            "last_login": "null"
        }
        response_data = {
            "username": "new_test_username",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "password": "new_password",
            "is_active": False
        }
        response = self.client.put(self.path, request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_data)

    def test_patch_request(self):
        request_data = {
            "username": "new_test_username",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "password": "new_password",
            "is_active": False,
            "last_login": "null"
        }
        response_data = {
            "username": "new_test_username",
            "first_name": "new_first_name",
            "last_name": "new_last_name",
            "password": "new_password",
            "is_active": False
        }
        response = self.client.patch(self.path, request_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_data)

    def test_delete_request(self):
        response = self.client.delete(self.path)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(str(User.objects.all()), "<QuerySet []>")
