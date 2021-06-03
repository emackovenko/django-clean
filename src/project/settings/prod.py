from .common import *
import datetime
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['*']

DEFAULT_RENDERER_CLASSES = ('rest_framework.renderers.JSONRenderer',)

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    )
}

DATABASES = {
    'default': dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)
}

CORS_ORIGIN_WHITELIST = [
]
