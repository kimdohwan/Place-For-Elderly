import os
import json

# - 주요 디렉토리 경로를 변수로 관리
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ROOT_DIR = os.path.dirname(BASE_DIR)
SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# - 비공개로 관리할 부분은 secrets 를 통해 관리
secrets_base = json.load(open(os.path.join(SECRET_DIR, 'base.json')))
SECRET_KEY = secrets_base['SECRET_KEY']


# =====================================================================================================================
# - dev/production 에 따라서 설정 변경
# - dev/production 공통사항은 이곳에 설정, 그 외 추가사항은 각각의 모듈에 설정
# - 공통사항 설정 항목 : DEBUG, DATABASE, ALLOWED_HOST, WSGI_APPLICATION

from config.settings import MODULE_NAME

secrets_module = json.load(open(os.path.join(SECRET_DIR, f'{MODULE_NAME}.json')))

DEBUG = True if not MODULE_NAME == 'production' else False

ALLOWED_HOSTS = secrets_module["ALLOWED_HOSTS"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WSGI_APPLICATION = f'config.wsgi.{MODULE_NAME}.application'

# =====================================================================================================================


# 기본 유져 모델 설정
AUTH_USER_MODEL = 'members.User'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'facilities',
    'members',
    'crispy_forms',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR
        ],
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

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
