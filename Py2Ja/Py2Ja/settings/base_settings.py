# -*- coding: utf-8 -*-
"""
Django settings for Py2Ja project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$3n5(g9cub5)_&c!#kx!=09(hzt&ge@myd6fjv$yn9^zqlky)l'

ALLOWED_INCLUDE_ROOTS = [os.path.join(BASE_DIR, 'html'), ]


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'entry',
    'blog',
    'program',
    'usr',
    'knowledge',

    'markdown_deux',
    'upload_avatar',
    'docutils',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Py2Ja.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/default')],
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
    # {
    #     'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #     'DIRS': [os.path.join(BASE_DIR, 'templates/jinja2')],
    #     'APP_DIRS': True,
    #     'OPTIONS': {
    #         'context_processors': [
    #             'django.template.context_processors.debug',
    #             'django.template.context_processors.request',
    #             'django.contrib.auth.context_processors.auth',
    #             'django.contrib.messages.context_processors.messages',
    #         ],
    #     },
    # },
]

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

WSGI_APPLICATION = 'Py2Ja.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Auth

# LOGIN_URL = ''
# LOGIN_REDIRECT_URL = ''


# Email

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'summychou@gmail.com'
EMAIL_HOST_PASSWORD = 'zhou88270273'
EMAIL_SUBJECT_PREFIX = '[Py2Ja]'
EMAIL_USE_TLS = True


# Logging


# django-upload-avatar

UPLOAD_AVATAR_UPLOAD_ROOT = os.path.join(BASE_DIR, 'media/uploaded_images')
UPLOAD_AVATAR_AVATAR_ROOT = os.path.join(BASE_DIR, 'media/cropped_avatars')
UPLOAD_AVATAR_URL_PREFIX_ORIGINAL = MEDIA_URL + 'uploaded_images/'
UPLOAD_AVATAR_URL_PREFIX_CROPPED = MEDIA_URL + 'cropped_avatars/'

UPLOAD_AVATAR_MAX_SIZE = 1024 * 1024 * 1  # 1MB
UPLOAD_AVATAR_RESIZE_SIZE = [40, 120]
UPLOAD_AVATAR_SAVE_FORMAT = 'jpg'

UPLOAD_AVATAR_DELETE_ORIGINAL_AFTER_CROP = True

UPLOAD_AVATAR_WEB_LAYOUT = {
    'preview_areas': [
        {
            'size': 40,
            'text': u'小头像'
        },
        {
            'size': 120,
            'text': u'大头像'
        },
    ]
}

UPLOAD_AVATAR_TEXT = {
    'CHOOSE_IMAGE': '选择图片',
    'CROP_IMAGE': '确认上传',
    'TEST_FUNC_NOT_PASSED': 'Forbidden',
    'INVALID_IMAGE': '图片无效，请重新选择',
    'NO_IMAGE': '请加载图片',
    'TOO_LARGE': '图片太大了，换张小的吧',
    'SUCCESS': '上传成功',
    'ERROR': '上传失败，请稍后再试',
}


# Django Grapplli
# https://django-grappelli.readthedocs.org/en/latest/

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
GRAPPELLI_ADMIN_TITLE = "Py2Ja"
GRAPPELLI_SWITCH_USER = True
