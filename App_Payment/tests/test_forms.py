from django.test import TestCase
from App_Payment.forms import BillingForm
from django.urls import reverse
from django.test import Client

class BillingFormTests(TestCase):
    def test_validation_do_not_accept_blanks(self):
        form = BillingForm(data={})
        self.assertTrue(form.is_valid())
