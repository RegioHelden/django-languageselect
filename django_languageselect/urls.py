# -*- coding: UTF-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^\?", views.IndexView.as_view(), name="languageselect_index"),
]
