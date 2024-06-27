=====================
django_languageselect
=====================


.. image:: https://img.shields.io/pypi/v/django_languageselect.svg
        :target: https://pypi.python.org/pypi/django_languageselect

.. image:: https://github.com/RegioHelden/django-languageselect/actions/workflows/build.yml/badge.svg
        :target: https://github.com/RegioHelden/django-languageselect/actions


Simple language select as custom template tag

Requirements
============

- "django.middleware.locale.LocaleMiddleware" in MIDDLEWARE_CLASSES / MIDDLEWARE
- "django.core.context_processors.request" in TEMPLATE_CONTEXT_PROCESSORS / TEMPLATES['OPTIONS']['context_processors']
- Add 'django_languageselect', to INSTALLED_APPS

Usage:
======

To use django_languageselect in a project, add it to `INSTALLED_APP`

```python
INSTALLED_APP  = [
    *INSTALLED_APP,
    'django_languageselect',
]
```

Add this to your urls.py

```python
urlpatterns = [
    *urlpatterns,
    url(r'^languageselect/', include('django_languageselect.urls')),
]
```

Use the languageselect tag where you which to show languages list:

```jinja
{% load languageselect %}

{% languageselect %}
```

Routes:
=======

The only url provided by this application is "languageselect_index". Required GET-parameter is "language", optional GET-parameter is "next". Next contains the named url to redirect after the language change. This parameter is pre-filled with the current page url.
Customization

Feel free to use your own template, just add languageselect/layer.html

* Free software: MIT license
* Documentation: https://django-languageselect.readthedocs.io.

Tests
=====

Tests will be automatically run by travis on commit to master.

They can also be executed locally using docker-compose by running `docker-compose up`

Making a new release
====================

bumpversion_ is used to manage releases.

.. _bumpversion: https://github.com/peritus/bumpversion

Add your changes to the HISTORY_ and run `docker-compose run --rm python bumpversion <major|minor|patch>`, then push (including tags)

.. _HISTORY: ./HISTORY.rst
