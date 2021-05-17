from django.test import TestCase
from App_Order.views import add_to_cart
# from .forms import Transaction
from django.urls import reverse
from django.test import Client

class App_Order_AddToCartViewTests(TestCase):
    def test_App_Order_add_to_cart_loads_properly(self):
        response = self.client.get(reverse('App_Order:add'))
        self.assertEqual(response.status_code,200)

class App_Order_CartViewTests(TestCase):
    def test_App_Order_cart_view_loads_properly(self):
        response = self.client.get(reverse('App_Order:cart'))
        self.assertEqual(response.status_code,302)

class App_Order_RemoveFromCartViewTests(TestCase):
    def test_App_Order_remove_from_cart_loads_properly(self):
        response = self.client.get(reverse('App_Order:remove'))
        self.assertEqual(response.status_code,200)

class App_Order_IncreaseCartViewTests(TestCase):
    def test_App_Order_increase_cart_loads_properly(self):
        response = self.client.get(reverse('App_Order:increase'))
        self.assertEqual(response.status_code,200)

class App_Order_DecreaseCartViewTests(TestCase):
    def test_App_Order_decrease_cart_loads_properly(self):
        response = self.client.get(reverse('App_Order:decrease'))
        self.assertEqual(response.status_code,200)
