from django.test import TestCase
from django.contrib.auth.models import User  # , Group

from .models import Organization
from reseller.models import Reseller


# to satisfy LoginRequiredMixin
# self.client.login(username='org', password='ramramtau')  # returns True if successful
# or
# self.client.force_login(user=org)  # returns True if successful


class OrganizationTestCase(TestCase):
    """
    Tests for organization
    """

    def setUp(self):
        orga = User.objects.create_user('orga', 'john@john.com', 'ramramtau')
        orgb = User.objects.create_user('orgb', 'john@john.com', 'ramramtau')
        resellerUser = User.objects.create_user('john', 'john@john.com', 'ramramtau')

        rslr = Reseller.objects.create(user=resellerUser)
        Organization.objects.create(name="Org A", reseller=rslr, user=orga)
        Organization.objects.create(name="Org B", reseller=rslr, user=orgb)

    def test_only_org_can_access_dashboard(self):
        # try to login with a reseller # verify rejected
        # self.client.login(request)
        # try to login with a superadmin # verify rejected
        # try to login with an organization # verify accepted
        pass

    # def test_group_organization_exists(self):
    #     """
    #     Group Organization needs to exists for the checks on the
    #     organization.views.OrganizationTestMixin level to work.
    #     """
    #     self.assertEqual(Group.objects.filter(name__icontains='Organization').exists(), True)
