from django.test import TestCase
from django.contrib.auth.models import User

from .models import Reseller
from organization.models import Organization


class ResellerViewsTestCase(TestCase):

    """tests for reseller views"""

    def setUp(self):
        user = User.objects.create_user('john', 'john@john.com', 'ramramtau')
        org_a = User.objects.create_user('orga', 'john@john.com', 'ramramtau')
        org_b = User.objects.create_user('orgb', 'john@john.com', 'ramramtau')
        rslr = Reseller.objects.create(user=user)
        Organization.objects.create(name="Org A", reseller=rslr, user=org_a)
        Organization.objects.create(name="Org B", reseller=rslr, user=org_b)

    def test_only_reseller_can_access_dashboard(self):
        # try to login with a superadmin # verify rejected
        # try to login with an organization # verify rejected
        # try to login with a reseller # verify accepted
        pass
