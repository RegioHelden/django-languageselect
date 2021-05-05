from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect

from . import forms


class IndexView(View):
    def get(self, request):
        next = "/"
        if "next" in request.GET:
            next = request.GET.get("next")

        response = HttpResponseRedirect(next)

        if not request.GET:
            return response

        form = forms.LanguageCodeForm(data=request.GET)
        if not form.is_valid():
            return response

        language = form.cleaned_data["language"]

        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            language,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )

        return response
