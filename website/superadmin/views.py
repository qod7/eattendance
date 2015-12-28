from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "superadmin/dashboard.html"


class ListResellersView(TemplateView):
    template_name = "superadmin/list_resellers.html"


class CreateResellerView(TemplateView):
    template_name = "superadmin/create_reseller.html"


class SettingsView(TemplateView):
    template_name = "superadmin/settings.html"
