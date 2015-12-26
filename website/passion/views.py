from django.views.generic import TemplateView


class HomeView(TemplateView):

    '''Just to test base.html'''

    template_name = "layout/base.html"
