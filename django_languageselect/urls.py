from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r"^\?", views.IndexView.as_view(), name="languageselect_index"),
]
