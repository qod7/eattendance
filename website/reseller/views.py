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

    """
    Dashboard that shows overall statistics.
    """
    template_name = "reseller/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Dashboard"
        return context


class ListOrganizationsView(ResellerTestMixin, TemplateView):

    """
    Lists the current organizations with various fields.
    """
    template_name = "reseller/list_organizations.html"

    def get_context_data(self, **kwargs):
        context = super(ListOrganizationsView, self).get_context_data(**kwargs)
        context['title'] = "List Organizations"
        return context


class AddOrganizationsView(ResellerTestMixin, TemplateView):

    """
    Shows a form to add a organization.
    """
    template_name = "reseller/add_organization.html"

    def get_context_data(self, **kwargs):
        context = super(AddOrganizationsView, self).get_context_data(**kwargs)
        context['title'] = "Add an Organization"
        return context


class SettingsView(ResellerTestMixin, TemplateView):

    """
    Edit user settings.
    - Change Password
    - Change email address
    - Change first_name and last_name
    """
    template_name = "reseller/settings.html"

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['title'] = "Settings"
        return context
