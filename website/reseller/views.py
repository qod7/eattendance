from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.core.urlresolvers import reverse

from organization.models import Organization, Staff, Attendance

from .models import Reseller
from .forms import AddOrganizationForm


class ResellerTestMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Checks if user is logged in and if user is a reseller.

    If user passes this test, the user has a reseller related object. So, he is a reseller.
    If user fails it, he is redirected to login.
    At login, if he is superadmin or organization, he's taken to his respective dashboard.
    If the user is none of those, he's logged out and informed his account is deleted.
    """

    def test_func(self):
        try:
            return self.request.user.reseller
        except Reseller.DoesNotExist:
            return False


class HomeView(ResellerTestMixin, TemplateView):
    """
    Dashboard that shows overall statistics.
    """
    template_name = "reseller/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        self.reseller = self.request.user.reseller
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = "Dashboard"
        context['organization_count'] = Organization.objects.filter(reseller=self.reseller).count()
        context['staff_count'] = Staff.objects.filter(organization__reseller=self.reseller).count()
        try:
            Staff.objects.get(organization__reseller=self.reseller)
        except (Staff.DoesNotExist, Staff.MultipleObjectsReturned):
            context['attendance_count'] = 0
        else:
            context['attendance_count'] = Attendance.objects.filter(staff__organization__reseller=self.reseller).count()
        return context


class ListOrganizationsView(ResellerTestMixin, ListView):
    """
    Lists the current organizations with various fields.
    """

    context_object_name = 'organization_list'
    template_name = "reseller/list_organizations.html"

    def post(self, request, *args, **kwargs):
        if 'deactivate' in self.request.POST:
            pass

        if 'activate' in self.request.POST:
            pass

        return super(ListOrganizationsView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListOrganizationsView, self).get_context_data(**kwargs)
        context['title'] = "List Organizations"
        return context

    def get_queryset(self):
        return Organization.objects.select_related('user').all()


class AddOrganizationView(ResellerTestMixin, FormView):
    """
    Shows and processes form to add an organization.
    """
    template_name = 'reseller/add_organization.html'
    form_class = AddOrganizationForm

    def get_success_url(self):
        messages.success(self.request, 'New organization has been added successfully!')
        messages.success(self.request, 'Login credentials have been emailed.')
        return reverse('reseller:list_organizations')

    def form_valid(self, form):
        form.save(reseller=self.request.user.reseller)
        # form.send_email()
        return super(AddOrganizationView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddOrganizationView, self).get_context_data(**kwargs)
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
