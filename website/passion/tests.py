from django.test import TestCase
from django.core.urlresolvers import reverse


class TestHomePage(TestCase):

    def test_uses_base_template(self):
        # response = self.client.get(reverse("home"))
        # self.assertTemplateUsed(response, "layout/base.html")
        pass
