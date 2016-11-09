from .staging import *


AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '{{ cookiecutter.aws_storage_bucket_name }}')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
