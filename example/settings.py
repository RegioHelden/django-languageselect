from django.conf import global_settings

SECRET_KEY = "*B&T*&^T867t^TB*^&T&%^RV%^re654e$^%CVE$^%E"  # noqa: S105

INSTALLED_APPS = (
    "django.contrib.sessions",
    "django_languageselect",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {},
    },
]

MIDDLEWARE = global_settings.MIDDLEWARE

ROOT_URLCONF = "django_languageselect.urls"
