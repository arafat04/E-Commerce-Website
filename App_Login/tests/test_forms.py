from django.test import TestCase
from App_Login.forms import ProfileForm,SignUpForm
from django.urls import reverse
from django.test import Client

class ProfileFormTests(TestCase):
    def test_validation_do_not_accept_blanks(self):
        form = ProfileForm(data={})
        self.assertTrue(form.is_valid())

class SignUpFormTests(TestCase):
    def test_validation_do_not_accept_blanks(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
