# Django settings for paraserry project.
import os
import sys

from django.conf.global_settings import *

import paraserry as project_module

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================


APP_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir,os.pardir))
DATA_DIR = os.path.join(APP_DIR, 'data')
LIBS_DIR = os.path.join(APP_DIR, 'libs')
PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
PYTHON_BIN = os.path.dirname(sys.executable)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))

if os.path.exists(os.path.join(PYTHON_BIN, 'activate_this.py')):
    VAR_ROOT = os.path.join(os.path.dirname(PYTHON_BIN), 'var')
elif ve_path and os.path.exists(os.path.join(ve_path, 'bin',
        'activate_this.py')):
    VAR_ROOT = os.path.join(ve_path, 'var')
else:
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)


#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'EST'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 2

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True



#==============================================================================
# Media settings
#==============================================================================

DEFAULT_FILE_STORAGE    = 'storages.backends.s3boto.S3BotoStorage'
if 'AWS_ACCESS_KEY_ID_SKP' not in os.environ:
    sys.exit('please define the AWS_ACCESS_KEY_ID_SKP.')

if 'AWS_SECRET_ACCESS_KEY_SKP' not in os.environ:
    sys.exit('please define the AWS_SECRET_ACCESS_KEY_SKP.')

AWS_ACCESS_KEY_ID       = os.environ['AWS_ACCESS_KEY_ID_SKP']
AWS_SECRET_ACCESS_KEY   = os.environ['AWS_SECRET_ACCESS_KEY_SKP']
AWS_STORAGE_BUCKET_NAME = 'paraserry'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(VAR_ROOT, 'static')
MEDIA_ROOT = os.path.join(VAR_ROOT, 'media')

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'media'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

#==============================================================================
# Add venv libs
#==============================================================================

VENV_SRC_DIR = os.path.join(APP_DIR, 'venv', 'src')

VENV_LIBS_DIR =  os.path.join(VENV_SRC_DIR, 'django-linksets')
sys.path.append(VENV_LIBS_DIR)



#==============================================================================
# Databases
#==============================================================================

#==============================================================================
# PRODUCTION DATABASE
#==============================================================================
# DATABASES = {
#      'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': "fw-postgres-01.cb9juhksq1bh.us-east-1.rds.amazonaws.com",
#         'NAME': "fw_prod",
#         'USER': "bigbellie",
#         'PASSWORD': "De1iv3r3d2014",
#         'PORT': '5432',
#      },
# }

#==============================================================================
# LOCAL DATBASE
#==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/Users/paraserry/paraserry/paraserry/db.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# DATABASES = {
#      'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'HOST': "fw-postgres-02.cb9juhksq1bh.us-east-1.rds.amazonaws.com",
#         'NAME': "fw_dev",
#         'USER': "a6Bd8q3DBt3JVPy3",
#         'PASSWORD': "CNZX65UzQKY5RjGN",
#         'PORT': '5432',
#      },
# }



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'in()yg@w0o*3^^0^sa^&amp;v2_+o4!)vygid#ulil_!=$%0g^u8-*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'paraserry.urls'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)


INSTALLED_APPS = (
    'grappelli',
    'grappelli.dashboard',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',

    'south',
    'linksets',
    'paraserry.apps.website',
    'paraserry.apps.media',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
}
GRAPPELLI_ADMIN_TITLE = "paraserry.com"


