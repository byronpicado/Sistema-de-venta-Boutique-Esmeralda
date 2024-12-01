from .base import *
from decouple import config

from .utils.logging_config import ANSIColorFormatter

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': config('DB_NAME'),
        'HOST': config('DB_HOST'),
        # 'PORT': '1220',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes',
        },
    }
}


# Configura los detalles de conexión a Papertrail
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'custom_format': {
            '()': ANSIColorFormatter,
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',  # Formato de fecha y hora
        },
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado
        },
        'papertrail': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'custom_format',  # Usa el formato personalizado para Papertrail
            'address': (config('HOST_PAPERTRAIL'), int(config('PORT_PAPERTRAIL'))),
        },
    },
    'root': {
        'handlers': ['console', 'papertrail'],
        'level': 'DEBUG',
    },
}