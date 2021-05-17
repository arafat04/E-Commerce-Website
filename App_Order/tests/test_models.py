from django.test import TestCase
from App_Order.models import Cart, Order
from App_Shop.models import Product

class CartModelTests(TestCase):
    def test__str__(self):
        item = Product(name="T-shirt")
        item.save()
        quantity = Cart(item =item, quantity=2)
        quanity.save()
        obj = Cart.objects.get(id=1)
        self.assertEqual(obj.__str__(),"T-shirt X 2")
    def test_get_total(self):
        self.price = 200
        self.quantity = 2
        total = self.price * self.quantity
        self.assertEqual(total, 400)


class OrderModelTests(TestCase):
    def test_get_totals(self):
        price = 200
        quantity = 5
        total = price * quantity
        self.assertEqual(total,1000)
