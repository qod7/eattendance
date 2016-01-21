from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django import forms

from .forms import GenericUserCreationForm


class GenericUserCreationFormTestCase(TestCase):

    def setUp(self):
        User.objects.create_user('existing', 'existing@existing.com', 'ramramtau')

    def test_first_name_too_long(self):
        first_name = "thisisaverylongfirstnamehopefullyitsnotallowed"
        last_name = "valid"
        email = "valid@valid.com"

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        form = GenericUserCreationForm(form_data)

        self.assertFalse(form.is_valid())
        # self.assertEquals(form.errors['first_name'], ["First name is too long."])

    def test_last_name_too_long(self):
        first_name = "valid"
        last_name = "thisisaverylonglastnamehopefullyitsnotallowed"
        email = "valid@valid.com"

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        form = GenericUserCreationForm(form_data)

        self.assertFalse(form.is_valid())
        # self.assertEquals(form.errors['last_name'], ["Last name is too long."])

    def test_existing_email(self):
        first_name = "valid"
        last_name = "valid"
        email = 'existing@existing.com'

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        form = GenericUserCreationForm(form_data)

        self.assertFalse(form.is_valid())
        # self.assertFormError(form.errors['email'], "Email address")

    def test_invalid_email(self):
        first_name = "valid"
        last_name = "valid"
        email = 'invalid@invalid'

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        form = GenericUserCreationForm(form_data)

        self.assertFalse(form.is_valid())

    def test_valid_form(self):
        first_name = "valid"
        last_name = "valid"
        email = "valid@valid.com"

        form_data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
        }

        form = GenericUserCreationForm(form_data)
        self.assertTrue(form.is_valid())

        user = form.save()
        self.assertNotEqual(user, None)

    def test_create_user(self):
        pass

    def test_email_to_user(self):
        # sends email
        # username in email
        # password in email
        pass
