# -*- coding: UTF-8 -*-
try:
    from django.urls import re_path  # noqa
except ImportError:
    from django.conf.urls import url  # noqa
    re_path = url

from . import views

urlpatterns = [
    re_path(r"^\?", views.IndexView.as_view(), name="languageselect_index"),
]
