'''
Settings module for Project.
'''
from pathlib import Path
from os import environ

from blogproject.apps import DJANGO_APPS, THIRD_PARTY_APPS, CUSTOM_APPS
from blogproject.middleware import DJANGO_MIDDLEWARE, THIRD_PARTY_MIDDLEWARE

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY: str = environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG: bool = bool(environ['DEBUG'])

ALLOWED_HOSTS = ['localhost']


# Application definition
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + CUSTOM_APPS
MIDDLEWARE = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogproject.wsgi.application'
ASGI_APPLICATION = 'blogproject.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ['DATABASE'],
        'USER': environ['USER'],
        'PASSWORD': environ['PASSWORD'],
        'HOST': environ['HOST'],
        'PORT': environ['PORT']
    },
    'developer': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    'noSQL': {
        'ENGINE': 'djongo',
        'NAME': environ['DATABASE']
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console'],
            'level': 'INFO'
        }
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE: str = environ["LANGUAGE_CODE"]

TIME_ZONE: str = environ["TIME_ZONE"]

USE_I18N: bool = bool(environ["USE_I18N"])

USE_TZ: bool = bool(environ["USE_TZ"])


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'userapp.User'
CORS_ALLOW_ALL_ORIGINS = True
