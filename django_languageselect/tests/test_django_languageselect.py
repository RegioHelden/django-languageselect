from django.conf import settings
from django.template import Context, Template
from django.test import Client, SimpleTestCase
from django.urls import reverse


class TestDjangoLanguageSelect(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_change_language_cookie(self):
        response = self.client.get(reverse("languageselect_index"), data={"language": "de"}, follow=False)
        self.assertEqual(response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, "de")
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse("languageselect_index"), data={"language": "en"}, follow=False)
        self.assertEqual(response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, "en")
        self.assertEqual(response.status_code, 302)

    def test_wrong_language_does_nothing(self):
        response = self.client.get(reverse("languageselect_index"), data={"language": "dsdsdsd"}, follow=False)
        self.assertTrue(settings.LANGUAGE_COOKIE_NAME not in response.client.cookies)
        self.assertEqual(response.status_code, 302)

    def test_next_url(self):
        next_url = "/whatever/"
        response = self.client.get(
            reverse("languageselect_index"),
            data={"language": "de", "next": next_url},
            follow=True,
        )
        self.assertEqual(response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, "de")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.redirect_chain[0][0], next_url)

    def test_no_params_does_nothing(self):
        response = self.client.get(reverse("languageselect_index"), follow=False)
        self.assertTrue(settings.LANGUAGE_COOKIE_NAME not in response.client.cookies)
        self.assertEqual(response.status_code, 302)

    def test_template_tag(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: "de"})
        response = self.client.get(reverse("languageselect_index"), follow=False)
        out = Template(
            "{% load languageselect %}{% languageselect %}",
        ).render(Context({"request": response.wsgi_request}))
        self.assertIn("django-languageselect-container", out)
