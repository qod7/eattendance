from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SuperAdminTestMixin(LoginRequiredMixin, UserPassesTestMixin):

    """
    Checks if user is logged in and if user is a superadmin
    """

    def test_func(self):
        return self.request.user.is_staff


class HomeView(SuperAdminTestMixin, TemplateView):

    """
    Dashboard that shows overall statistics.
    """
    template_name = "superadmin/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Dashboard"
        return context


class ListResellersView(SuperAdminTestMixin, TemplateView):

    """
    Lists the current resellers with various fields.
    """
    template_name = "superadmin/list_resellers.html"

    def get_context_data(self, **kwargs):
        context = super(ListResellersView, self).get_context_data(**kwargs)
        context['title'] = "List Resellers"
        return context


class AddResellerView(SuperAdminTestMixin, TemplateView):

    """
    Shows a form to add a reseller.
    """
    template_name = "superadmin/add_reseller.html"

    def get_context_data(self, **kwargs):
        context = super(AddResellerView, self).get_context_data(**kwargs)
        context['title'] = "Add a Reseller"
        return context


class SettingsView(SuperAdminTestMixin, TemplateView):

    """
    Edit user settings.
    - Change Password
    - Change email address
    - Change first_name and last_name
    """
    template_name = "superadmin/settings.html"

    def get_context_data(self, **kwargs):
        context = super(SettingsView, self).get_context_data(**kwargs)
        context['title'] = "Settings"
        return context
