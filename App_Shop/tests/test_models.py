from django.test import TestCase
from App_Shop.models import Category, Product
from django.urls import reverse
from django.test import Client



# Create your tests here.

class CategoryrModelTests(TestCase):

    def test__str__(self):
        title = Category(
            title = 'Amp'
        )
        self.assertEqual(str(title),"Amp")

class ProductModelTests(TestCase):

    def test__str__(self):
        name = Product(
            name = 'White Shirt'
        )
        self.assertEqual(str(name),"White Shirt")
