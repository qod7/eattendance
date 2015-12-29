from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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

    def test_reseller_dashboard(self):
        response = self.client.get(reverse('reseller:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Reseller")
        # self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_only_logged_in_user_can_access_dashboard(self):
        # try to access dashboard without authenticated user
        # assert falsse
        # authenticate a user
        # log in with the user
        # try to access dashboard

        pass

    def test_only_reseller_can_access_dashboard(self):
        # try to login with a superadmin # verify rejected
        # try to login with an organization # verify rejected
        # try to login with a reseller # verify accepted
        pass

    def test_list_organization(self):
        pass
