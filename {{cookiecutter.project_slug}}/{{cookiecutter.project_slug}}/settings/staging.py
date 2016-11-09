import os
from .base import *


DEBUG = False
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
INSTALLED_APPS += (
    'storages',
)
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_AUTO_CREATE_BUCKET = True

AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '{{ cookiecutter.aws_storage_bucket_name }}_staging')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
