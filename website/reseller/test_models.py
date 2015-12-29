import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Reseller
from organization.models import Organization


class ResellerModelsTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('john', 'john@john.com', 'ramramtau')
        org_a = User.objects.create_user('orga', 'john@john.com', 'ramramtau')
        org_b = User.objects.create_user('orgb', 'john@john.com', 'ramramtau')
        rslr = Reseller.objects.create(user=user)
        Organization.objects.create(name="Org A", reseller=rslr, user=org_a)
        Organization.objects.create(name="Org B", reseller=rslr, user=org_b)

    def test_reseller_default_values(self):
        """
        Test whether reseller is created correctly with default values
        """
        rslr = Reseller.objects.first()
        self.assertEqual(rslr.contact, "")
        self.assertEqual(rslr.remarks, "")
        self.assertEqual(rslr.expiry_date.year, (datetime.datetime.now() + datetime.timedelta(weeks=52)).year)

    def test_reseller_disable(self):
        rslr = Reseller.objects.first()
        rslr.deactivate_account()
        self.assertEqual(rslr.user.is_active, False)

    def test_reseller_enable(self):
        rslr = Reseller.objects.first()
        rslr.activate_account()
        self.assertEqual(rslr.user.is_active, True)

    def test_reseller_org_count(self):
        rslr = Reseller.objects.first()
        self.assertEqual(rslr.organization_count(), 2)

    def test_reseller_can_create_org(self):
        """
        Can the reseller from setup create any organizations?
        """
        rslr = Reseller.objects.first()
        self.assertEqual(rslr.can_create_organization(), False)
