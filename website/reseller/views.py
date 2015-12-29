from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class ResellerTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a reseller.

    If user passes this test, the user has a reseller related object. So, he is a reseller.
    If user fails it, he is redirected to login.
    At login, if he is superadmin or organization, he's taken to his respective dashboard.
    If the user is none of those, he's logged out and informed his account is deleted.
    """

    def test_func(self):
        return self.request.user.reseller


class HomeView(ResellerTestMixin, TemplateView):
    template_name = "reseller/base.html"
