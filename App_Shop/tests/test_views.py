from django.test import TestCase
from App_Shop.views import Home, ProductDetail
from django.urls import reverse
from django.test import Client

class App_Shop_HomeViewTests(TestCase):
    client = Client()
    def test_App_Shop_Home_loads_properly(self):
        response = self.client.get(reverse('App_Shop/home.html'))
        self.assertEqual(response.status_code, 200)

class App_Shop_ProductDetailTests(TestCase):
    client = Client()
    def test_App_Shop_ProductDetail_loads_properly(self):
        response = self.client.get(reverse('App_Shop/product_detail.html'))
        self.assertEqual(response.status_code, 200)
