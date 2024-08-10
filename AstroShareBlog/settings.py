"""
Django settings for AstroShareBlog project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os

os.environ['CLOUDINARY_CLOUD_NAME'] = 'dtbji5cfz'
os.environ['CLOUDINARY_API_KEY'] = '839441162297935'
os.environ['CLOUDINARY_API_SECRET'] = 'eTQFu1X9X065YP1jycD8d4aMSJc'
                                      

from pathlib import Path
import cloudinary
import cloudinary.uploader
import cloudinary.api
# from cloudinary.models import CloudinaryField

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

database_url = os.environ.get("DATABASE_URL")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

#SECRET_KEY = 'django-insecure-1ieo2(r5opy@dl(xqzlm0^xti0vnz85)81chvvakz@$q@om!7)'
DATABASE_URL = 'postgres://uwb4hdjzua9:7p5Hb6Ee1XKE@ep-gentle-mountain-a23bxz6h.eu-central-1.aws.neon.tech/trait_shore_zero_528265'

SECRET_KEY = 'django-insecure-m@=5yl8r(&a%ez6c5#le$5%za(cqckq#53bvnl^)24-p3zgobe'

CLOUDINARY_URL = "CLOUDINARY_URL"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['8000-harmonicame-astroshareb-tykmah5chi5.ws.codeinstitute-ide.net',
                 '.herokuapp.com']

CSRF_TRUSTED_ORIGINS = [
       'https://8000-harmonicame-astroshareb-tykmah5chi5.ws.codeinstitute-ide.net',
    ]
    
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogger',
    'members',   
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'AstroShareBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'AstroShareBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_REDIRECT_URL = 'frontpage-blogpost'
LOGOUT_REDIRECT_URL = 'frontpage-blogpost'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'filip.vanelslande@gmail.com'
EMAIL_HOST_PASSWORD = 'xfmz ofjm gvib ljvu'
DEFAULT_FROM_EMAIL = 'filip.vanelslande@gmail.com'
SITE_URL = 'https://mail.vanelslande.com:444'

