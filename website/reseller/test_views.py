from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import Reseller
from organization.models import Organization


class ResellerViewsTestCase(TestCase):
    """Tests for reseller.views"""

    def setUp(self):
        user = User.objects.create_user('john', 'john@john.com', 'ramramtau')
        org_a = User.objects.create_user('orga', 'john@john.com', 'ramramtau')
        org_b = User.objects.create_user('orgb', 'john@john.com', 'ramramtau')
        rslr = Reseller.objects.create(user=user)
        Organization.objects.create(name="Org A", reseller=rslr, user=org_a)
        Organization.objects.create(name="Org B", reseller=rslr, user=org_b)

    def test_reseller_dashboard(self):
        response = self.client.get(reverse('reseller:home'))
        self.assertEqual(response.status_code, 302)
        self.assertContains(response, "Reseller")
        # self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_only_logged_in_user_can_access_dashboard(self):
        # try to access dashboard without authenticated user
        # response = self.client.post('/login/', {'username': 'john', 'password': 'smith'})
        # assert false
        # response.status_code
        # response = c.get('/customer/details/')
        # response.content
        # response.context['name']
        # /customers/details/?name=fred&age=7
        # c.get('/customers/details/', {'name': 'fred', 'age': 7})
        # response = c.get('/redirect_me/', follow=True)
        # response.redirect_chain
        # c.post('/login/', {'name': 'fred', 'passwd': 'secret'})
        # response.json()['name']
        # response.template
        # c.login(username='fred', password='secret')
        # returns True
        # c.logout()

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


# class EmailTest(TestCase):

#     def test_send_email(self):
#         # Send message.
#         mail.send_mail('Subject here', 'Here is the message.',
#                        'from@example.com', ['to@example.com'],
#                        fail_silently=False)

#         # Test that one message has been sent.
#         self.assertEqual(len(mail.outbox), 1)

#         # Verify that the subject of the first message is correct.
#         self.assertEqual(mail.outbox[0].subject, 'Subject here')
