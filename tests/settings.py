import django.conf.global_settings as DEFAULT_SETTINGS


SECRET_KEY = 'amazingsecretkey'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'django_languageselect',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
]

MIDDLEWARE = DEFAULT_SETTINGS.MIDDLEWARE

ROOT_URLCONF = 'django_languageselect.urls'
