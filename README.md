# django-languageselect

Simple language select as custom template tag.
Requires "django.core.context_processors.request" in TEMPLATE_CONTEXT_PROCESSORS.

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
