from django.test import TestCase
from django.contrib.auth.models import User

from organization.models import Organization
from reseller.models import Reseller


class OrganizationTestCase(TestCase):

    """
    Tests for organization
    """

    def setUp(self):
        user = User.objects.create_user('john', 'john@john.com', 'ramramtau')
        rslr = Reseller.objects.create(user=user)
        Organization.objects.create(name="Org A", reseller=rslr)
        Organization.objects.create(name="Org B", reseller=rslr)

    def test_only_superadmin_can_access_dashboard(self):
        # try to login with a reseller # verify rejected
        # try to login with an organization # verify rejected
        # try to login with a superadmin # verify accepted
        pass


class AddResellerFormTestCase(object):
    """Tests for AddResellerForm"""

    def test_template_rendered(self):
        pass

    def test_submitting_form_with_long_first_name(self):
        pass

    def test_submitting_form_with_long_last_name(self):
        pass

    def test_form_with_invalid_email(self):
        pass

    def test_existing_email_address(self):
        pass

    def test_select_option_not_in_list(self):
        pass

    def test_valid_form(self):
        # redirects correctly
        # shows message
        pass

    def test_email_to_reseller(self):
        # sends email
        # username in email
        # password in email
        pass
