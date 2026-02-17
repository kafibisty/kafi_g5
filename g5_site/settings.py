import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!wtugoe_5g5a7ah(l*$%q&)bobps7m!wn8z$0$s6j^n6pcf$w^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# রেন্ডারে চালানোর জন্য এটি অবশ্যই '*' অথবা আপনার ডোমেইন হতে হবে
ALLOWED_HOSTS = ['*'] 

# Application definition
INSTALLED_APPS = [
    'products',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # দ্বিতীয় লাইনে এটি যোগ করা হয়েছে
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'g5_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'g5_site.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# লগইন সেটিংস
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# ফাইলের একদম নিচে এটি যোগ করা হয়েছে (অনলাইনে সিএসএস দেখানোর জন্য)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# রেন্ডারে সাবমিট করার সময় নিচের সিকিউরিটি লাইনটি প্রয়োজন হতে পারে
CSRF_TRUSTED_ORIGINS = ['https://*.onrender.com']