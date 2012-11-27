# -*- coding: UTF-8 -*-

from django.views.generic import View
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils import translation
import forms


class IndexView(View):
	def get(self, request):
		# determine redirect
		next = "index"
		if "next" in request.GET:
			next = request.GET.get("next")

		response = HttpResponseRedirect(next)

		# process language change
		if request.GET:
			form = forms.LanguageCodeForm(data=request.GET)

			if form.is_valid():
				language = form.cleaned_data['language']
				if hasattr(request, "session"):
					request.session["django_language"] = language
				else:
					response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
				translation.activate(language)

		return response
