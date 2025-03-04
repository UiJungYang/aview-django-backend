"""
Django settings for av_db project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

from django.conf.global_settings import CSRF_TRUSTED_ORIGINS
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    'corsheaders',
    'rest_framework',
    'kakao_oauth',
    'account',
    'account_profile',
    'survey',
    'company_report',
    'cart',
    'orders',
    'marketing',
    'interview',
    'interview_result',
    'authentication',
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', '').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv('CSRF_TRUSTED_ORIGINS', '').split(',')
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:8080",
# ]
print('CORS_ALLOWED_ORIGINS:', CORS_ALLOWED_ORIGINS)

# CORS 설정 옵션
CORS_ALLOW_CREDENTIALS = True

# CORS 헤더와 메서드 추가 설정 (필요 시)
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-request-with',
]

KAKAO = {
    'LOGIN_URL': os.getenv('KAKAO_LOGIN_URL'),
    'CLIENT_ID': os.getenv('KAKAO_CLIENT_ID'),
    'REDIRECT_URI': os.getenv('KAKAO_REDIRECT_URI'),
    'TOKEN_REQUEST_URI': os.getenv('KAKAO_TOKEN_REQUEST_URI'),
    'USER_INFO_REQUEST_URI': os.getenv('KAKAO_USERINFO_REQUEST_URI'),
}

GOOGLE = {
    'LOGIN_URL': os.getenv('GOOGLE_LOGIN_URL'),
    'CLIENT_ID': os.getenv('GOOGLE_CLIENT_ID'),
    'CLIENT_SECRET': os.getenv('GOOGLE_CLIENT_SECRET'),
    'REDIRECT_URI': os.getenv('GOOGLE_REDIRECT_URI'),
    'TOKEN_REQUEST_URI': os.getenv('GOOGLE_TOKEN_REQUEST_URI'),
    'USER_INFO_REQUEST_URI': os.getenv('GOOGLE_USERINFO_REQUEST_URI')
}

NAVER ={
    'LOGIN_URL': os.getenv('NAVER_LOGIN_URL'),
    'CLIENT_ID': os.getenv('NAVER_CLIENT_ID'),
    'CLIENT_SECRET': os.getenv("NAVER_CLIENT_SECRET"),
    'REDIRECT_URI': os.getenv('NAVER_REDIRECT_URI'),
    'TOKEN_REQUEST_URI': os.getenv('NAVER_TOKEN_REQUEST_URI'),
    'USER_INFO_REQUEST_URI': os.getenv('NAVER_USERINFO_REQUEST_URI'),
}

ROOT_URLCONF = "av_db.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

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

WSGI_APPLICATION = "av_db.wsgi.application"

# redis 사용시 주석 해제
# REDIS_HOST = os.getenv('REDIS_HOST')
# REDIS_PORT = os.getenv('REDIS_PORT')
# REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
#
# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/0',  # Redis의 0번 DB를 사용합니다. 필요에 따라 DB 번호를 수정할 수 있습니다.
#         'OPTIONS': {
#             'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#             'PASSWORD': REDIS_PASSWORD,  # Redis 비밀번호를 설정합니다.
#             'SOCKET_CONNECT_TIMEOUT': 5,  # Redis 서버와의 연결 시도 제한 시간을 설정합니다.
#         }
#     }
# }


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# MySQL Settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv('DATABASE_NAME'),
        "USER": os.getenv('DATABASE_USER'),
        "PASSWORD": os.getenv('DATABASE_PASSWORD'),
        "HOST": os.getenv('DATABASE_HOST'),
        "PORT": os.getenv('DATABASE_PORT'),
        "OPTIONS": { "charset": "utf8mb4" },
    }
}

REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PASSWORD': REDIS_PASSWORD,
            'SOCKET_CONNECT_TIMEOUT': 5,
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
