from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import AddResellerForm


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


class AddResellerView(SuperAdminTestMixin, FormView):

    """
    Shows and processes form to add a reseller.
    """
    template_name = 'superadmin/add_reseller.html'
    form_class = AddResellerForm

    def get_success_url(self):
        return reverse('superadmin:list_resellers')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(AddResellerView, self).form_valid(form)

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
