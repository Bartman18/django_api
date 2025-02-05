
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase


#
# User = get_user_model()
# class RegisterViewTest(APITestCase):
#     def setUp(self):
#         self.register_url = '/api/register/'
#         self.login_url = '/api/login/'
#         self.logout_url = '/api/logout/'
#         self.valid_user_data = {
#             "email": "user@test.com",
#             "first_name": "user",
#             "last_name": "user",
#             "phone_number": "111222333",
#             "password": "Test",
#             "password2": "Test",
#
#         }
#
#     # def test_register_user(self):
#     #     response = self.client.post(self.register_url, data=self.valid_user_data, format='json')
#     #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#     #
#     #
#     #     self.assertIn("access", response.data)
#     #     self.assertIn("refresh", response.data)
#     #
#     #
#     #     check_user = User.objects.get(email=self.valid_user_data["email"])
#     #     self.assertEqual(check_user.email, self.valid_user_data["email"])
#
#     def test_register_and_login(self):
#
#         register_data = {
#             "email": "testuser@example.com",
#             "first_name": "Test",
#             "last_name": "User",
#             "phone_number": "123456789",
#             "password": "TestPassword123",
#             "password2": "TestPassword123"
#         }
#         register_response = self.client.post(self.register_url, register_data, format="json")
#
#         self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)
#         self.assertIn("access", register_response.data)
#
#
#         login_data = {
#             "email": register_data["email"],
#             "password": register_data["password"]
#         }
#         login_response = self.client.post(self.login_url, login_data, format="json")
#
#         self.assertEqual(login_response.status_code, status.HTTP_200_OK)
#         self.assertIn("access", login_response.data)
#         self.assertIn("refresh", login_response.data)
#
#
#         user = User.objects.get(email=register_data["email"])
#         self.assertIsNotNone(user)
#
#         access_token = login_response.data["access"]
#         self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
#
#
#


# class AddProductViewTest(APITestCase):
#     def setUp(self):
#         # Tworzymy superusera, korzystając z Twojego custom user managera
#         User = get_user_model()
#         self.admin_user = User.objects.create_superuser(
#             email='admin@example.com',
#             password='adminpass',
#             first_name='Admin',
#             last_name='User',
#             phone_number='123456789'
#         )
#         # Uwierzytelniamy klienta jako superusera
#         self.client.force_authenticate(user=self.admin_user)
#
#         self.add_product_url = '/api/add_product/'
#         self.product_data = {
#             "product_id": 23,  # Upewnij się, że pole odpowiada temu, co oczekuje serializer
#             "name": "baton",
#             "price": 23,
#         }
#
#     def test_add_product(self):
#         response = self.client.post(self.add_product_url, self.product_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertIn("product_id", response.data)