from django.test import TestCase
from App_Payment.views import checkout
# from .forms import Transaction
from django.urls import reverse
from django.test import Client

class App_Payment_CheckOutViewTests(TestCase):
    client = Client()
    def setUp(self) -> None:
        self.saved_address = 'testaddress'
        self.order_items = 'shirt'
        self.order_total = 2
    def test_App_Payment_checkout_loads_properly(self):
        response = self.client.get(reverse('App_Payment:checkout'))
        self.assertEqual(response.status_code, 302)

class App_Payment_PaymentViewTests(TestCase):
    def test_App_Payment_payment_loads_properly(self):
        response = self.client.get(reverse('App_Payment:checkout'))
        self.assertEqual(response.status_code, 302)
