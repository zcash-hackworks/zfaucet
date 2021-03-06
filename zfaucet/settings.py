"""
Django settings for zfaucet project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'prod')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/
# ENVIRONMENT = os.getenv('DJANGO_ENVIRONMENT', 'dev')
if ENVIRONMENT not in ['dev', 'stage', 'prod']:
        raise Exception('Unknown settings environment "%s"' % ENVIRONMENT)
print('settings environment is {}'.format(ENVIRONMENT))

# SECURITY WARNING: keep the secret key used in production secret!
#if ENVIRONMENT == 'prod':
#        SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
#else:

# These secrets are written by Ansible during provisioning.
SECRET_KEY = os.getenv('SECRET_KEY', 'badsecret')
DJANGO_POSTGRESQL_USER = os.getenv('DJANGO_POSTGRESQL_USER', 'django')
DJANGO_POSTGRESQL_PASSWORD = os.getenv('DJANGO_POSTGRESQL_PASSWORD', '')
DJANGO_POSTGRESQL_HOST = os.getenv('DJANGO_POSTGRESQL_HOST', 'localhost')
ZCASH_NETWORK = os.getenv('ZCASH_NETWORK', 'http://localhost:18232')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIRONMENT == 'dev'


# production
ALLOWED_HOSTS = ['faucet.testnet.z.cash', '127.0.0.1']
if os.getenv('ZFAUCET_HOSTNAME'):
    ALLOWED_HOSTS.append(os.getenv('ZFAUCET_HOSTNAME'))

# Application definition

INSTALLED_APPS = [
    'faucet',
    'zfaucet',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

if ENVIRONMENT == 'dev':
    INSTALLED_APPS.append('django.contrib.admin')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'zfaucet.urls'

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

WSGI_APPLICATION = 'zfaucet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

if ENVIRONMENT == 'dev':
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                        'OPTIONS': {
                                'timeout': 10,
                        },
                },
        }
else:
        # prod and stage
        DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.postgresql_psycopg2',
                        'NAME': 'django',
                        'USER': DJANGO_POSTGRESQL_USER,
                        'PASSWORD': DJANGO_POSTGRESQL_PASSWORD,
                        'HOST': DJANGO_POSTGRESQL_HOST,
                        'PORT': '5432',
                        'CONN_MAX_AGE': 3600,
                },
        }



# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = '/home/zcashd/zfaucet/faucet/static'
DONATION_ORG = 'Electric Coin Co'