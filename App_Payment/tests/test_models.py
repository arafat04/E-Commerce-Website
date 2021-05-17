from django.test import TestCase
from App_Payment.models import BillingAddress
from App_Login.models import Profile
from django.urls import reverse
from django.test import Client



# Create your tests here.

class BillingAddressModelTests(TestCase):
    def test__str__(self):
        name = "Arafat"
        self.assertEqual(str(name), "Arafat")
    def test_is_fully_filled(self):
        t = Profile(
        address_1="Dhaka",zipcode="1212",city="Dhaka",country="Bangladesh"
        )
        self.assertIs(t.is_fully_filled(),False)
