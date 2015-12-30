from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth.models import User  # , AnonymousUser
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.core import mail

from organization.models import Organization
from reseller.models import Reseller

from .views import LoginView


class LoginTestCase(TestCase):

    """Tests for Login"""
    # todo: test own functions by simulating HttpRequests

    def setUp(self):
        org = User.objects.create_user('org', 'john@john.com', 'ramramtau')
        reseller = User.objects.create_user('reseller', 'john@john.com', 'ramramtau')
        superadmin = User.objects.create_user('superadmin', 'john@john.com', 'ramramtau')
        deactivated_user = User.objects.create_user('deac', 'john@john.com', 'ramramtau')
        User.objects.create_user('nogrp', 'john@john.com', 'ramramtau')

        rslr = Reseller.objects.create(user=reseller)
        Organization.objects.create(name="Org A", reseller=rslr, user=org)

        superadmin.is_staff = True
        superadmin.save()

        deactivated_user.is_active = False
        deactivated_user.save()

        self.factory = RequestFactory()

    def test_template_used(self):
        """
        Test if login.html is used when get request is sent to account:login
        """
        # anonymous user
        response = self.client.get(reverse("account:login"))
        self.assertTemplateUsed(response, "useraccounts/login.html")
        self.assertEqual(response.context['title'], "Login")
        self.assertContains(response, "<title>Passion: Login</title>")

        # authenticated user
        request = self.factory.get(reverse("account:login"))
        request.user = auth.authenticate(username='superadmin', password='ramramtau')

        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        """
        Test if user can log in correctly.
        Note: This is pretty useless since it's actually testing auth.authenticate :D
        """
        existing_user = auth.authenticate(username='org', password='ramramtau')
        non_existing_user = auth.authenticate(username='orga', password='ramramtau')

        self.assertNotEqual(existing_user, None)
        self.assertEqual(non_existing_user, None)

    def test_org_login(self):
        """
        Test if user org can log in and is correctly redirected.
        User created in setUp inside test db.
        """
        response = self.client.post(reverse("account:login"),
                                    {'username': 'org', 'password': 'ramramtau'},
                                    follow=True
                                    )
        self.assertNotContains(response, "Invalid username or password")
        self.assertRedirects(response, reverse('organization:home'))

        # self.assertEqual(response.redirect_chain, [('/organization/', 302)])
        # self.assertEqual(Organization.objects.filter(user=user).exists(), True)

    def test_reseller_login(self):
        """
        Reseller log in and redirection.
        """
        response = self.client.post(reverse("account:login"),
                                    {'username': 'reseller', 'password': 'ramramtau'},
                                    follow=True
                                    )
        self.assertNotContains(response, "Invalid username or password")
        self.assertRedirects(response, reverse('reseller:home'))

    def test_superadmin_login(self):
        """
        Superadmin login and redirection.
        """
        response = self.client.post(reverse("account:login"),
                                    {'username': 'superadmin', 'password': 'ramramtau'},
                                    follow=True
                                    )
        self.assertNotContains(response, "Invalid username or password")
        self.assertRedirects(response, reverse('superadmin:home'))

    def test_user_with_no_group_login(self):
        """
        This user is not a: superadmin, reseller, organization
        """
        response = self.client.post(reverse("account:login"),
                                    {'username': 'nogrp', 'password': 'ramramtau'},
                                    follow=True
                                    )
        self.assertContains(response, "Your account has been deleted.")

    def test_deactivated_user_login(self):
        """
        Deactivated user should get msg about deactivation.
        """
        response = self.client.post(reverse("account:login"),
                                    {'username': 'deac', 'password': 'ramramtau'},
                                    follow=True
                                    )
        self.assertContains(response, "Sorry, your account has been deactivated.")


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class ForgotPasswordTestCase(TestCase):

    """
    Tests for Forgot Password
    """

    def setUp(self):
        User.objects.create_user('a', 'john@john.com', 'ramramtau')
        User.objects.create_user('b', 'bob@bob.com', 'ramramtau')
        User.objects.create_user('c', 'bob@bob.com', 'ramramtau')

    def test_get_request_to_reset_password(self):
        """
        Get request to this view should return nothing.
        """
        # todo: prevent get request in the view code itself. then check 404

        response = self.client.get(reverse("account:reset_password"),
                                   {'email': 'john@john.com'},
                                   follow=True,)
        self.assertEqual(response.content, b'')

    def test_post_request_to_reset_password(self):
        """
        The view only accepts post requests.
        Test with existing and non-existing email address in the db
        """
        # entered email doesn't exist in db
        response = self.client.post(reverse("account:reset_password"),
                                    {'email': 'mike@mike.com'},
                                    follow=True,)
        # should still get the same response
        self.assertTemplateUsed(response, "useraccounts/login.html")
        self.assertContains(response, "emailed you instructions for resetting your password.")

        # entered email exists in db
        response = self.client.post(reverse("account:reset_password"),
                                    {'email': 'john@john.com'},
                                    follow=True,)
        self.assertTemplateUsed(response, "useraccounts/login.html")
        self.assertContains(response, "emailed you instructions for resetting your password.")

        # for some reason the following is not working
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Password reset on Passion')
        self.assertIn("password reset for your user account at Passion.", mail.outbox[0].body)

        # todo: get the url from the email and check the response

    def test_two_accounts_same_email_forgot_password(self):
        """
        It sends two emails with different links for each account.
        """
        self.client.post(reverse("account:reset_password"),
                         {'email': 'bob@bob.com'},
                         follow=True,)

        self.assertEqual(len(mail.outbox), 2)

    def test_reset_confirm_template_used(self):
        response = self.client.get(reverse("account:password_reset_confirm",
                                           args={'Mg', '484-aece2515580f9d316f41'}))
        self.assertTemplateUsed(response, "useraccounts/password_reset/password_reset_confirm.html")
        self.assertEqual(response.context['title'], "Password reset unsuccessful")
