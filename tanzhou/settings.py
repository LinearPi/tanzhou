"""
Django settings for tanzhou project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tq7jx2qll*81ch^q383o$(q-h^5^je7x*qn+t@1-8j%$mri%)u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

AUTH_USER_MODEL = 'users.UserInfo'


AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users.apps.UsersConfig',
    'course',
    'bootstrap4',
    'captcha',
    'pure_pagination',
    'ckeditor',    # 富文本的使用
    'ckeditor_uploader',

]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tanzhou.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                 'django.template.context_processors.media',  # 这个是用来配置media的路径
            ],
        },
    },
]

WSGI_APPLICATION = 'tanzhou.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tanzhoudb',
        'USER': 'develop',
        'PASSWORD': 'QWEqwe123',
        'HOST': '192.168.83.128',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 3,
    'MARGIN_PAGES_DISPLAYED': 1,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# QQ 邮箱发送
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 465  # SSL  # 第三种配置方式
# EMAIL_PORT = 587  #  TSL  # 第二种配置方式
# EMAIL_PORT = 25   #第一种配置方式
EMAIL_HOST_USER = "3003002865@qq.com"
EMAIL_HOST_PASSWORD = "xtyxxnyonltqdfgf"
# EMAIL_USE_TLS = True  #第一种配置方式 # 第二种配置方式
EMAIL_USE_SSL = True   #第三种配置方式
EMAIL_FROM = "3003002865@qq.com"

#  配置关于文件上传的设置
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# 关于ckediter富文本的配置
# 只上传图片文件
CKEDITOR_ALLOW_NONIMAGE_FILES = False
# 上传路径设置
CKEDITOR_UPLOAD_PATH = "uploads/"
# 用于文件上传
CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
# 富文本的内容
CKEDITOR_CONFIGS = {
    'default_ckeditor': {
        'skin': 'moono',
        'toolbar': 'Full',
        'height': 300,
        'width': '100%' ,
    },
    'awesome_ckeditor': {
        'toolbar': 'Basic',
    },
}

