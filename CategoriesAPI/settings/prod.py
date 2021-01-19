from .base import *

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('AUTH_DATABASE_NAME'),
        'HOST': os.environ.get('AUTH_DATABASE_HOST'),
        'PORT': os.environ.get('AUTH_DATABASE_PORT'),
        'USER': os.environ.get('AUTH_DATABASE_USER'),
        'PASSWORD': os.environ.get('AUTH_DATABASE_PASSWORD'),
    }
}
