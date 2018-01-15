=====================
django_languageselect
=====================


.. image:: https://img.shields.io/pypi/v/django_languageselect.svg
        :target: https://pypi.python.org/pypi/django_languageselect

.. image:: https://img.shields.io/travis/RegioHelden/django-languageselect.svg
        :target: https://travis-ci.org/RegioHelden/django-languageselect

.. image:: https://readthedocs.org/projects/django-languageselect/badge/?version=latest
        :target: https://django-languageselect.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Simple language select as custom template tag


Requirements
============

- "django.middleware.locale.LocaleMiddleware" in MIDDLEWARE_CLASSES
- "django.core.context_processors.request" in TEMPLATE_CONTEXT_PROCESSORS
- Add 'django_languageselect', to INSTALLED_APPS

Usage:
======

{% load languageselect %}
{% languageselect %}

Routes:
=======

The only url provided by this application is "languageselect_index". Required GET-parameter is "language", optional GET-parameter is "next". Next contains the named url to redirect after the language change. This parameter is pre-filled with the current page url.
Customization

Feel free to use your own template, just add languageselect/layer.html


* Free software: MIT license
* Documentation: https://django-languageselect.readthedocs.io.
