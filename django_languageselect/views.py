# -*- coding: UTF-8 -*-

from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation
import forms


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

        language = form.cleaned_data['language']
        if not translation.check_for_language(language):
            return response

        if hasattr(request, "session"):
            request.session[translation.LANGUAGE_SESSION_KEY] = language
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        translation.activate(language)

        return response
