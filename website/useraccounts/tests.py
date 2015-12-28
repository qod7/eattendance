from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib import auth

from organization.models import Organization
from reseller.models import Reseller


class LoginTestCase(TestCase):

    """Tests for Login"""
    # todo: test own functions by simulating HttpRequests

    def setUp(self):
        org = User.objects.create_user('org', 'john@john.com', 'ramramtau')
        reseller = User.objects.create_user('reseller', 'john@john.com', 'ramramtau')
        superadmin = User.objects.create_user('superadmin', 'john@john.com', 'ramramtau')
        deactivated_user = User.objects.create_user('deac', 'john@john.com', 'ramramtau')

        rslr = Reseller.objects.create(user=reseller)
        Organization.objects.create(name="Org A", reseller=rslr, user=org)

        superadmin.is_staff = True
        superadmin.save()

        deactivated_user.is_active = False
        deactivated_user.save()

    def test_login(self):
        user = auth.authenticate(username='org', password='ramramtau')
        self.assertNotEqual(user, 'None')

    def test_org_login(self):
        user = auth.authenticate(username='org', password='ramramtau')
        self.assertEqual(Organization.objects.filter(user=user).exists(), True)

    def test_resller_login(self):
        user = auth.authenticate(username='reseller', password='ramramtau')
        self.assertEqual(Reseller.objects.filter(user=user).exists(), True)

    def test_superadmin_login(self):
        user = auth.authenticate(username='superadmin', password='ramramtau')
        self.assertEqual(user.is_staff, True)

    def test_deactivated_user_login(self):
        user = auth.authenticate(username='deac', password='ramramtau')
        self.assertEqual(user.username, 'deac')
