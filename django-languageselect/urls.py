# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r"^\?", views.IndexView.as_view(), name="languageselect_index"),
)
