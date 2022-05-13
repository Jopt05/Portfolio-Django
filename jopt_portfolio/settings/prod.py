from .base import *
import dj_database_url
from decouple import config
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    'https://jopt05.github.io',
    'http://jopt05.github.io',
    'jopt05.github.io',
    'https://www.jopt05.github.io',
    'http://www.jopt05.github.io',
    'www.jopt05.github.io',
    'https://www.jopt05.github.io/portfolio/',
    'http://www.jopt05.github.io/portfolio/',
    'www.jopt05.github.io/portfolio/',
    'http://192.168.100.138',
    '192.168.100.138',
]

CORS_ALLOWED_ORIGINS = [
    'https://jopt05.github.io',
    'http://jopt05.github.io',
    'jopt05.github.io',
    'https://www.jopt05.github.io',
    'http://www.jopt05.github.io',
    'www.jopt05.github.io',
    'https://www.jopt05.github.io/portfolio/',
    'http://www.jopt05.github.io/portfolio/',
    'www.jopt05.github.io/portfolio/',
    'http://192.168.100.138',
    '192.168.100.138',
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
