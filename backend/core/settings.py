"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import configparser
import os
from datetime import date

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Config
config = configparser.ConfigParser()
config.read(os.path.join(BASE_DIR, "core/config.ini"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4ghla6qff%h!$0ly*od86+kgw&(vu2ve1bmkm6a^lcp0961q7k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'captcha', # django-simple-captcha 
    'recaptcha', # django-recaptcha
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

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Django-allauth
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'  # 當用戶登入時，既可以使用使用者名稱也可以使用email
ACCOUNT_EMAIL_REQUIRED = True  # 註冊時必須填寫email
ACCOUNT_EMAIL_VERIFICATION = "mandatory" # 若email沒有驗證,則無法登入
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5 # 失敗的登錄嘗試次數。超過此數量時，將禁止用戶在指定的ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT秒數內登錄。
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300 # 秒
LOGIN_REDIRECT_URL = '/' # 設定登入後跳轉連結
LOGIN_URL = '/accounts/login/' # default login url

ACCOUNT_RATE_LIMITS = {
    # Change password view (for users already logged in)
    "change_password": "5/m",
    # Email management (e.g. add, remove, change primary)
    "manage_email": "10/m",
    # Request a password reset, global rate limit per IP
    "reset_password": "20/m",
    # Rate limit measured per individual email address
    "reset_password_email": "5/m",
    # Password reset (the view the password reset email links to).
    "reset_password_from_key": "20/m",
    # Signups.
    "signup": "20/m",
    # NOTE: Login is already protected via `ACCOUNT_LOGIN_ATTEMPTS_LIMIT`
}

CAPTCHA_METHOD_LIST = ["django-simple-captcha", "django-recaptcha"]
CAPTCHA_METHOD = "django-simple-captcha"

RECAPTCHA_PUBLIC_KEY = config['Google-reCaptchaV2']['client_secret_key']
RECAPTCHA_PRIVATE_KEY = config['Google-reCaptchaV2']['server_secret_key']
# RECAPTCHA_PROXY  = { 'http' : 'http://127.0.0.1:8000' , 'https' : 'https://127.0.0.1:8000' }
# SILENCED_SYSTEM_CHECKS  = [ 'captcha.recaptcha_test_key_error' ]

# captcha
ACCOUNT_FORMS = {
    "login": "account.forms.RecaptchaLoginForm",
    "signup": "account.forms.CustomSignupForm",
}


# SMTP Configuration
EMAIL_HOST = 'smtp.gmail.com'  # 這裡使用QQ的smtp服務
EMAIL_PORT = 587
EMAIL_HOST_USER = config["GMAIL"]["email"]
EMAIL_HOST_PASSWORD = config["GMAIL"]["password"]
EMAIL_USE_TLS = True  # 這裡必須是 True，否則傳送不成功
DEFAULT_FROM_EMAIL = 'b10202225@gmail.com'    # 預設發件人郵箱

# Django_extensions - Graph 
GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# LOGGING

# SET LOG
logname = "log"
if logname not in os.listdir(BASE_DIR):
    os.mkdir(logname)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'new_add': {
            '()': 'middleware.middlewares.RequestLogFilter',
        }
    },
    'formatters':{
        'info-formatter': {
            'format': '[%(asctime)s][%(source_ip)s] %(levelname)s : %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers':{
        'file': {
            'level': 'INFO',
            'formatter': 'info-formatter',
            'filters': ['new_add'],
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, logname, f'{str(date.today())}.txt'),
    },
    'console': {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
    },
    'app-logger': {
        'handlers': ['file', 'console'],
        'level': 'CRITICAL',
        'propagate': True,
        },
    },
}

# GEOIP2
GEOIP_PATH = os.path.join(BASE_DIR)

