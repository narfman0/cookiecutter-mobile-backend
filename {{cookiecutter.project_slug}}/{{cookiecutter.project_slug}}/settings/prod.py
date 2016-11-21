from .staging import *


AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '{{ cookiecutter.aws_storage_bucket_name }}')
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
        'NAME': os.environ.get('DATABASE_NAME', '{{ cookiecutter.database_name }}'),
        'USER': os.environ.get('DATABASE_USER', '{{ cookiecutter.database_user }}'),
        'PASSWORD': os.environ.get('DATABASE_PASS', '{{ cookiecutter.database_pass }}'),
        'HOST': os.environ.get('DATABASE_HOST', '{{ cookiecutter.database_host }}'),
        'PORT': os.environ.get('DATABASE_PORT', '{{ cookiecutter.database_port }}'),
    }
}
