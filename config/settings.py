from pathlib import Path
from decouple import Config, RepositoryEnv
import os

# -------------------------------
# BASE
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Leer .env
config = Config(RepositoryEnv(BASE_DIR / ".env"))

# -------------------------------
# SEGURIDAD
# -------------------------------
SECRET_KEY = config('SECRET_KEY', default='unsafe-secret-key')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

# 🔥 Necesario para Render
CSRF_TRUSTED_ORIGINS = [
    'https://*.onrender.com'
]

# -------------------------------
# APPS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'libros',
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 🔥 WhiteNoise para producción
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# -------------------------------
# TEMPLATES
# -------------------------------
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

WSGI_APPLICATION = 'config.wsgi.application'

# -------------------------------
# BASE DE DATOS
# -------------------------------
# 🔥 LOCAL = MySQL
# 🔥 PRODUCCIÓN (Render) = SQLite

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# -------------------------------
# VALIDACIONES
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------
# IDIOMA
# -------------------------------
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'

USE_I18N = True
USE_TZ = True

# -------------------------------
# ARCHIVOS ESTÁTICOS
# -------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 🔥 WhiteNoise compresión
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------------
# ARCHIVOS MEDIA (IMÁGENES)
# -------------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# -------------------------------
# DEFAULT ID
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'