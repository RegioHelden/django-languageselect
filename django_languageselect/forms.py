from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import check_for_language


class LanguageCodeValidator:
    def __init__(self, value):
        if not value or not check_for_language(value):
            raise ValidationError("Invalid language code")


class LanguageCodeForm(forms.Form):
    language = forms.CharField(
        max_length=5,
        validators=[LanguageCodeValidator],
    )
