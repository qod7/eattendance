from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class OrganizationTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a organization.
    """

    def test_func(self):
        return self.request.user.organization


class HomeView(OrganizationTestMixin, TemplateView):
    template_name = "organization/base.html"
