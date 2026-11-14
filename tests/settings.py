SECRET_KEY = "DUMMY_SECRET_KEY"  # noqa: S105

# Application definition

PROJECT_APPS = ["charsleft_widget"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    *PROJECT_APPS,
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = "/static/"
