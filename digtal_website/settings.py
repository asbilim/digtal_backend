from datetime import timedelta
from pathlib import Path
import time
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%k$b-*!w&zv^4wv6(=swlxqn=t9-h^pt!@bf4m2h2!ri2tj%1s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CSRF_COOKIE_NAME = 'XSRF-TOKEN'
CSRF_HEADER_NAME = 'HTTP_X_XSRF_TOKEN'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'website'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digtal_website.urls'

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

WSGI_APPLICATION = 'digtal_website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # },
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
         'NAME':'jglzfans',
         'USER':'jglzfans',
         'PASSWORD':'jqJ9U2WCuBHlXqiB3Bu-G1Yd_aOQReSa',
         'HOST':'otto.db.elephantsql.com',
         'PORT':'5432',
    }
    # 'default':{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'dbs10236547',
    #     'USER': 'dbu5477858',
    #     'PASSWORD': 'Anepaspirater123@',
    #     'HOST': 'db5012165528.hosting-data.io',
    #     'PORT': '3306',
    # }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
}

year = time.gmtime(time.time()).tm_year


JAZZMIN_SETTINGS = {
    "site_title": "Digtal Admin Dashboard",
    "site_header": "Digtal Admin",
    "welcome_sign": "Welcome back Admin",
    "copyright": f"Digtal @{year}",
}



CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://0.0.0.0:3000",
    "http://127.0.0.0:3000",
    "http://127.0.0.0:3001",
    "http://127.0.0.0:3002",
    "http://172.20.10.4:3000",
]