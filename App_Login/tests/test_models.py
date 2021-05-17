from django.test import TestCase
from App_Login.models import Profile, MyUserManager,User
from django.urls import reverse
from django.test import Client



# Create your tests here.

class MyUserManagerModelTests(TestCase):

    def test_create_user(self):
        user = User.objects._create_user('arafatrahman@gmail.com', 'password123')
        self.assertTrue(isinstance(user, User))
    def test_create_superuser(self):
        user = User.objects.create_superuser('is_staff', 'is_superuser')
        self.assertTrue(isinstance(user, User))

class UserModelTests(TestCase):

    def test__str__(self):
        email = User(
            email = "arafatrahman04@gmail.com"
        )
        self.assertEqual(str(email), "arafatrahman04@gmail.com")

    def test_get_full_name(self):
        email = User(
            email = "arafatrahman04@gmail.com"
        )
        self.assertEqual(str(email), "arafatrahman04@gmail.com")

    def test_get_short_name(self):
        email = User(
            email = "arafatrahman04@gmail.com"
        )
        self.assertEqual(str(email), "arafatrahman04@gmail.com")


class ProfileModelTests(TestCase):

    def test__str__(self):
        t = Profile(username="Arafat")
        self.assertEqual(str(t), t.username+"'s Profile'")

    def test_is_fully_filled(self):
        t = Profile(
        address_1="Dhaka",zipcode="1212",city="Dhaka",country="Bangladesh"
        )
        self.assertIs(t.is_fully_filled(),False)
