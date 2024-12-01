import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta
from decouple import config

HOST_PAPERTRAIL = config('HOST_PAPERTRAIL')
PORT_PAPERTRAIL = config('PORT_PAPERTRAIL', cast=int)

# Cargar las variables de entorno desde el archivo .env
load_dotenv()  # Esto carga las variables de entorno definidas en el archivo .env

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mssql',
        'NAME': os.getenv('DB_NAME', 'BoutiqueEsmeraldaDB1'),  # Nombre de la base de datos
        'HOST': os.getenv('DB_HOST', 'DESKTOP-CAKRKLJ'),      # Nombre del host de la base de datos
        'PORT': os.getenv('DB_PORT', '1433'),  # Puerto predeterminado de SQL Server
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes',
        },
    }
}

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Importar configuraciones de apps personalizadas
from apps.catalogos.setting_apps import CATALOGOS_SETTING_APPS
from apps.seguridad.setting_apps import SEGURIDAD_SETTING_APPS
from apps.movimientos.setting_apps import MOVIMIENTOS_SETTING_APPS

# Quick-start development settings
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')  # Cargar la clave secreta desde las variables de entorno

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'rest_framework_simplejwt',
] + MOVIMIENTOS_SETTING_APPS + SEGURIDAD_SETTING_APPS + CATALOGOS_SETTING_APPS

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
        'DIRS': [],  # Agrega directorios de plantillas aquí si es necesario
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
"""
DATABASES = {
    'default': {
        'ENGINE': 'mssql',  # Utilizamos el backend mssql-django
        'NAME': 'tiseybd',  # Nombre de la base de datos
        'USER': 'tiseybd',  # Usuario de la base de datos
        'PASSWORD': '1234**',  # Contraseña de la base de datos
        'HOST': 'den1.mssql7.gear.host',  # IP del servidor SQL Server
        #'PORT': '1220',  # Puerto del servidor SQL Server (1433 es el predeterminado)
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # Especifica el driver ODBC que tienes instalado
            'extra_params': 'TrustServerCertificate=yes',  # Útil si estás usando SSL sin un certificado de confianza
        },
    }
}
"""
WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
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

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=50),  # Se puede extender el tiempo de vida
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Dependerá de la seguridad que necesites
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,  # Asegúrate de que SECRET_KEY esté bien protegido
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = './static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'usuarios.User'  # Asegúrate de que apunta a tu modelo de usuario personalizado
