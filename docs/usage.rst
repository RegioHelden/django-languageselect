=====
Usage
=====

To use django_languageselect in a project, add it to `INSTALLED_APP`

    'django_languageselect',

Add this to your urls.py

    url(r'^languageselect/', include('django_languageselect.urls')),

Use the languageselect tag where you which to show languages list:

    {% load languageselect %}
    {% languageselect %}