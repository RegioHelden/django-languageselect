# -*- coding: UTF-8 -*-

from django.conf.urls.defaults import *
from languageselect.views import IndexView

urlpatterns = patterns('',
	url(r"^/?", IndexView.as_view(), name="languageselect_index"),
)
