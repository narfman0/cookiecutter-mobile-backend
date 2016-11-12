import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.join('..', os.path.dirname(__file__)))

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.join('..', os.path.dirname(os.path.abspath(__file__))))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", 'c2$f9=w6rh=jo-2v7zv)mqqb#lf2%)v29nl8el0+gyfl#*8g-^')

ALLOWED_HOSTS = ['*',]
ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'
WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'
LANGUAGE_CODE = 'en'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = ()
SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    {% if cookiecutter.use_bootstrap == 'y' %}'aldryn_bootstrap3',{% endif %}
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_link',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_utils',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    '{{ cookiecutter.project_slug }}',
    'rest_framework',
    'djangocms_rest_api',
)

LANGUAGES = (
    ('en', gettext('en')),
)

CMS_LANGUAGES = {
    1: [
        {
            'name': gettext('en'),
            'public': True,
            'redirect_on_fallback': True,
            'hide_untranslated': False,
            'code': 'en',
        },
    ],
    'default': {
        'public': True,
        'redirect_on_fallback': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ('fullwidth.html', 'Fullwidth'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

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

MIGRATION_MODULES = {

}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)
