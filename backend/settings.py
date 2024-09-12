import os
from pathlib import Path
from tools.env import ENV

BASE_DIR = Path(__file__).resolve().parent.parent

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
SILENCED_SYSTEM_CHECKS = ["fields.W340"]

SECRET_KEY = ENV.secret_key()

#! ____________________ SEGURIDAD ____________________

DEBUG = ENV.debug()

# Permite todos los origenes en modo debug
ALLOWED_HOSTS = ["*"] if DEBUG else ENV.host()

# Acepta todos los origenes en modo debug
CORS_ALLOW_ALL_ORIGINS  = DEBUG

# Permite todas las credenciales cuando esta en produccion
CORS_ALLOW_CREDENTIALS  = DEBUG == False

# Permite todos los origenes en modo debug
CORS_ORIGIN_ALLOW_ALL   = DEBUG

# En modo debug no hay listas de origenes permitidos
CORS_ORIGIN_WHITELIST   = [] if DEBUG else ENV.cors()
CORS_ALLOWED_ORIGINS    = [] if DEBUG else ENV.cors()

# Permite cabeceras y metodos en modo debug y no
CORS_ALLOW_HEADERS      = "*"
CORS_ALLOW_METHODS      = "*"

#! ____________________ SEGURIDAD ____________________


INSTALLED_APPS=[
    # 'jet',
    'daphne',
    # 'jet.dashboard' if DEBUG else None,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'rest_framework.authtoken',
    'django_extensions',
    'corsheaders',
    'django_cleanup.apps.CleanupConfig',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'channels',
    'apps.common',
    'apps.party',
].__add__(ENV.apps_for_settings())

if DEBUG : INSTALLED_APPS.append('django.contrib.staticfiles')

DATABASES=ENV.connections()

# TODO: agregar tenants aquí
DATABASE_ROUTERS=[
    'tools.router.empresaUno_router',
]

REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES':(
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny'
    ),
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

MIDDLEWARE=[
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF='backend.urls'

TEMPLATES=[
    {
        'BACKEND':'django.template.backends.django.DjangoTemplates',
        'DIRS':[],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors':[
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION="backend.asgi.application"

if ENV.local() :
    CHANNEL_LAYERS={
        'default':{ 'BACKEND': "channels.layers.InMemoryChannelLayer" }
    }
else:
    CHANNEL_LAYERS={
        'default':{
            'BACKEND': 'channels_redis.core.RedisChannelLayer',
            'CONFIG': {
                'hosts': [('localhost', 6379)],
            },
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS=[
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE='es-pe'
TIME_ZONE='America/Lima'
USE_I18N=True
USE_TZ=True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR, 'media')

STATIC_URL='/static/'

if DEBUG:
    STATIC_ROOT=os.path.join(BASE_DIR, 'static')
    STATICFILES_DIRS=[os.path.join(BASE_DIR, 'staticfiles')]
else:
    STATIC_ROOT=os.path.join(BASE_DIR, 'static')