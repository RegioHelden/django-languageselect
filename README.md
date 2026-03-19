# django_languageselect

[![PyPI](https://img.shields.io/pypi/v/django_languageselect.svg)](https://pypi.python.org/pypi/django_languageselect)
[![PyPI](https://github.com/RegioHelden/django-languageselect/actions/workflows/build.yml/badge.svg)](https://github.com/RegioHelden/django-languageselect/actions)

Simple language select as custom template tag

## Requirements

- `"django.middleware.locale.LocaleMiddleware"` in `MIDDLEWARE_CLASSES` / `MIDDLEWARE`
- `"django.core.context_processors.request"` in `TEMPLATE_CONTEXT_PROCESSORS` / `TEMPLATES['OPTIONS']['context_processors']`

## Usage

To use django_languageselect in a project, add it to `INSTALLED_APP`

```python
INSTALLED_APP  = [
    *INSTALLED_APP,
    'django_languageselect',
]
```

Then add its endpoint to your `urls.py`. It's important to keep the `languageselect_index` name when using the provided template tag!

```python
from django.urls import path

from django_languageselect.views import IndexView

urlpatterns = [
    path("languageselect", IndexView.as_view(), name="languageselect_index"),
]
```

Use the languageselect template tag where you wish to show the language selection:

```jinja
{% load languageselect %}

{% languageselect %}
```

This will render all languages in your `LANGUAGES` setting to select from.

### Parameters

* `language` is the only required parameter expecting a two-letter ISO 639 language code.
* `next` - optionally pass the URL to redirect to after the language has been changed. The template tag redirects to the current URL.

### Customization

Feel free to use your own template, just add `languageselect/layer.html` to the template folder of an app that is earlier in your `INSTALLED_APP` than `django_languageselect`.

## Tests

Tests will be automatically run by travis on commit to master.

They can also be executed locally using docker-compose by running `docker-compose up`

## Making a new release

This project makes use of [RegioHelden's reusable GitHub workflows](https://github.com/RegioHelden/github-reusable-workflows). \
Make a new release by manually triggering the `Open release PR` workflow.
