# -*- coding: utf-8 -*-
import os

from util import get_env

PROJECT_NAME = u'NUKLEO'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ENV = get_env(BASE_DIR)

SECRET_KEY = ENV.get('SECRET_KEY', ENV.get('SECRET_KEY'))
DEBUG = True

ALLOWED_HOSTS = ENV.get('ALLOWED_HOSTS', [])
SITE_URL = ENV.get('URL_SITE', '')

# EMAIL
EMAIL_HOST = ENV.get('EMAIL_HOST', '')
EMAIL_HOST_USER = ENV.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = str(ENV.get('EMAIL_HOST_PASSWORD', ''))
DEFAULT_FROM_EMAIL = ENV.get('DEFAULT_FROM_EMAIL', '')
SERVER_EMAIL = ENV.get('SERVER_EMAIL', '')
EMAIL_PORT = ENV.get('EMAIL_PORT', '')
EMAIL_USE_TLS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ENV.get('DB_NAME'),
        'USER': ENV.get('DB_USER'),
        'PASSWORD': ENV.get('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)
# Para normalizar nombres de archivo en formato ASCII en vez de Unicode
DEFAULT_FILE_STORAGE = 'apps.core.util.storage.ASCIIFileSystemStorage'
DJANGO_APPS = [
    # solo las aplicaciones propias de django
    # 'grappelli.dashboard',
    # 'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
]

LOCAL_APPS = [
    # Aqui van las aplicaciones de  tu local ejem: apps.web
    'apps.web',
    'apps.core',
    'apps.redirects',
    'apps.seo',
]

THIRD_PART_APPS = [
    # Solo aplicaciones externas
    # 'debug_toolbar',
    'django_extensions',
    'filebrowser',
    'geoposition',
    'ckeditor',
    'ckeditor_uploader',
    'pytest',
    'mixer'
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PART_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.redirects.middleware.RedirectFallbackMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'apps.web.context_processor.web_processor',
            ],
        },
    },
]


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


STATIC_URL = '/static/'
STATIC_ROOT = ''

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Carpeta FileBrowser oculto en el admin
FILEBROWSER_SHOW_IN_DASHBOARD = False

ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'


LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# USE_THOUSAND_SEPARATOR = True
# THOUSAND_SEPARATOR = ','

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'apps.core.util.log.ColorizingStreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        }
    }
}

CKEDITOR_JQUERY_URL = '{}admin/js/vendor/jquery/jquery.js'.format(STATIC_URL)
CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
                ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                 'JustifyRight', 'JustifyBlock'],
                ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink", "Subscript", "Superscript"], ['Undo', 'Redo'], ["Source"],
                ["Maximize"]],
        # 'height': 300,
        # 'width': 300,
        # "removePlugins": "Bold",
    },
    'small': {
        'toolbar': [["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker", "Link", "Unlink"],
                ['NumberedList', 'BulletedList', "Indent", "Outdent", 'JustifyLeft', 'JustifyCenter',
                 'JustifyRight', 'JustifyBlock'],
                 ['Undo', 'Redo'], ["Source"],
                ["Maximize"]],
        'height': 100,
        # 'width': auto,
        "removePlugins": "Bold",
    },
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}

SITE_ID = 1
