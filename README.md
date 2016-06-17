# django-languageselect

Simple language select as custom template tag.

## Requirements
* "django.middleware.locale.LocaleMiddleware" in MIDDLEWARE_CLASSES
* "django.core.context_processors.request" in TEMPLATE_CONTEXT_PROCESSORS

Usage:
```django
{% load languageselect %}
{% languageselect %}
```

## Routes

The only url provided by this application is "languageselect_index".
Required GET-parameter is "language", optional GET-parameter is "next".
Next contains the named url to redirect after the language change.
This parameter is pre-filled with the current page url.

## Customization

Feel free to use your own template, just add languageselect/layer.html

## Changelog

0.1.3 Fix session key to store language, Django 1.9 compatibility
