from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse

from .forms import AddResellerForm

from reseller.models import Reseller
from organization.models import Organization, Staff, Attendance


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
        context['reseller_count'] = Reseller.objects.count()
        context['organization_count'] = Organization.objects.count()
        context['staff_count'] = Staff.objects.count()
        context['attendance_count'] = Attendance.objects.count()
        return context


class ResellerListView(SuperAdminTestMixin, ListView):

    """
    Lists the current resellers with various fields.
    """
    context_object_name = 'reseller_list'
    template_name = "superadmin/list_resellers.html"

    def get_context_data(self, **kwargs):
        context = super(ResellerListView, self).get_context_data(**kwargs)
        context['title'] = "List Resellers"
        return context

    def get_queryset(self):
        return Reseller.objects.select_related('user').all()


class AddResellerView(SuperAdminTestMixin, FormView):

    """
    Shows and processes form to add a reseller.
    """
    template_name = 'superadmin/add_reseller.html'
    form_class = AddResellerForm

    def get_success_url(self):
        messages.success(self.request, 'New reseller added successfully!')
        return reverse('superadmin:list_resellers')

    def form_valid(self, form):
        form.save(commit=False)
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
