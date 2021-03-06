"""
Django settings for cq project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!8xab&lqvxekvox48=x+(hqes27xf1(oojwvy-!p_8b@8g99(a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cityquest',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cq.urls'

WSGI_APPLICATION = 'cq.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'cq',
        'USER': 'root',
        'PASSWORD': 'ham7',
        'HOST': '',   # Or an IP Address that your DB is hosted on
        'PORT': '',
        'OPTIONS': {
             "init_command": "SET foreign_key_checks = 0;",
         },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Vancouver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

SITE_ROOT = os.path.dirname(__file__)
THUMBNAIL_DEBUG = True
MEDIA_ROOT = os.path.join(SITE_ROOT, 'userimg') #'/var/www/cq/userimg/'
MEDIA_URL = '/cq/userimg/'
STATIC_URL = '/cq/staticfiles/'
STATIC_ROOT = '/var/www/cq/staticfiles/'
STATICFILES_DIRS = (
    '/var/www/cq/cityquest/static',
)

TEMPLATE_DIRS = (
    '/var/www/cq/templates',
    '/var/www/cq/cityquest/templates/cityquest',
)

LOGIN_URL = '/cq/login/'

LOGIN_REDIRECT_URL = '/cq/cityquest/home'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)


AUTH_USER_MODEL = 'cityquest.UserProfile'
