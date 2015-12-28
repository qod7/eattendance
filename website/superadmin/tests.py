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
