import os
from .base import *


DEBUG = False
INSTALLED_APPS += (
    'storages',
)
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_AUTO_CREATE_BUCKET = True
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '{{ cookiecutter.aws_storage_bucket_name }}_staging')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATICFILES_STORAGE = '{{ cookiecutter.project_slug }}.settings.storage.StaticStorage'

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = '{{ cookiecutter.project_slug }}.settings.storage.MediaStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', '{{ cookiecutter.database_name }}_staging'),
        'USER': os.environ.get('DATABASE_USER', '{{ cookiecutter.database_user }}'),
        'PASSWORD': os.environ.get('DATABASE_PASS', '{{ cookiecutter.database_pass }}'),
        'HOST': os.environ.get('DATABASE_HOST', '{{ cookiecutter.database_host }}'),
        'PORT': os.environ.get('DATABASE_PORT', '{{ cookiecutter.database_port }}'),
    }
}
