from django.test import TestCase
from App_Login.views import sign_up
# from .forms import Transaction
from django.urls import reverse
from django.test import Client

class App_Login_SignUpViewTests(TestCase):
    client = Client()
    def setUp(self) -> None:
        self.username = 'testuser'
        self.email = 'testuser@email.com'
        self.password = 'password'
    def test_App_Login_signup_loads_properly(self):
        response = self.client.get(reverse('App_Login:signup'))
        self.assertEqual(response.status_code, 200)

class App_Login_LoginUserViewTests(TestCase):
    client = Client()
    def setUp(self) -> None:
        self.email = 'testuser@email.com'
        self.password = 'password'
    def test_App_Login_login_user_loads_properly(self):
        response = self.client.get(reverse('App_Login:login'))
        self.assertEqual(response.status_code, 200)

class App_Login_LogoutUserViewTests(TestCase):
    client = Client()
    def test_App_Login_logout_user_loads_properly(self):
        response = self.client.get(reverse('App_Login:logout'))
        self.assertEqual(response.status_code, 302)

class App_Login_UserProfileViewTests(TestCase):
    client = Client()
    def setUp(self) -> None:
        self.email = 'testuser@email.com'
        self.password = 'password'
        self.username = 'testuser'
    def test_App_Login_user_profile_loads_properly(self):
        response = self.client.get(reverse('App_Login:profile'))
        self.assertEqual(response.status_code, 302)
