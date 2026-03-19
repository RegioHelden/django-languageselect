from django.urls import path

from django_languageselect.views import IndexView

urlpatterns = [
    path("languageselect", IndexView.as_view(), name="languageselect_index"),
]
