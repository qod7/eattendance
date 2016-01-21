from django.test import TestCase, RequestFactory

from .forms import GenericUserCreationForm


class GenericUserCreationFormTestCase(TestCase):

    def setUp(self):
        pass

    def test_template_rendered(self):
        pass

    def test_create_user(self):
        pass

    def test_too_long_first_name(self):
        pass

    def test_too_long_last_name(self):
        pass

    def test_existing_email(self):
        pass

    def test_invalid_email(self):
        pass

    def test_valid_form(self):
        # redirects correctly
        # shows message
        pass

    def test_email_to_user(self):
        # sends email
        # username in email
        # password in email
        pass
