#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.template import Template, Context
from django.test import TestCase, Client
from django.utils import translation

try:
    from django.core.urlresolvers import reverse
except ImportError:
    from django.urls import reverse

if hasattr(settings, 'MIDDLEWARE_CLASSES'):
    MIDDELWARE_SETTINGS_NAME = 'MIDDLEWARE_CLASSES'
else:
    MIDDELWARE_SETTINGS_NAME = 'MIDDLEWARE'


class TestDjangoLanguageSelect(TestCase):
    def setUp(self):
        self.client = Client()

    def test_change_language_cookie(self):
        response = self.client.get(reverse('languageselect_index'), data={
            'language': 'de'}, follow=False)
        self.assertEqual(
            response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, 'de')
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('languageselect_index'), data={
            'language': 'en'}, follow=False)
        self.assertEqual(
            response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, 'en')
        self.assertEqual(response.status_code, 302)

    def test_change_language_session(self):
        with self.modify_settings(**{MIDDELWARE_SETTINGS_NAME: {
            'append': 'django.contrib.sessions.middleware.SessionMiddleware',
        }}):
            response = self.client.get(reverse('languageselect_index'), data={
                'language': 'de'}, follow=False)
            self.assertTrue(
                settings.LANGUAGE_COOKIE_NAME not in response.client.cookies)
            self.assertEqual(
                response.client.session[translation.LANGUAGE_SESSION_KEY],
                'de'
            )

            response = self.client.get(reverse('languageselect_index'), data={
                'language': 'fr'}, follow=False)
            self.assertEqual(
                response.client.session[translation.LANGUAGE_SESSION_KEY],
                'fr'
            )

    def test_wrong_language_does_nothing(self):
        response = self.client.get(reverse('languageselect_index'), data={
            'language': 'dsdsdsd'}, follow=False)
        self.assertTrue(
            settings.LANGUAGE_COOKIE_NAME not in response.client.cookies)
        self.assertEqual(response.status_code, 302)

    def test_next_url(self):
        next_url = '/whatever/'
        response = self.client.get(reverse('languageselect_index'),
                                   data={'language': 'de', 'next': next_url},
                                   follow=True)
        self.assertEqual(
            response.client.cookies[settings.LANGUAGE_COOKIE_NAME].value, 'de')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.redirect_chain[0][0], next_url)

    def test_no_params_does_nothing(self):
        response = self.client.get(
            reverse('languageselect_index'), follow=False)
        self.assertTrue(
            settings.LANGUAGE_COOKIE_NAME not in response.client.cookies)
        self.assertEqual(response.status_code, 302)

    def test_template_tag(self):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: 'de'})
        response = self.client.get(
            reverse('languageselect_index'), follow=False)
        out = Template(
            "{% load languageselect %}"
            "{% languageselect %}"
        ).render(Context({'request': response.wsgi_request}))
        self.assertIn('django-languageselect-container', out)
