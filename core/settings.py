# Import Path so Django can build file-system paths safely on Windows and other systems.
import os
from pathlib import Path
from dotenv import load_dotenv

# Define the project root directory from this settings file.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Development secret key; replace this with an environment variable before production.
SECRET_KEY = 'django-insecure-development-key-change-before-production'

# Keep debugging enabled while developing locally.
DEBUG = True

# Allow the local development server to respond to localhost and 127.0.0.1.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Register Django's built-in applications and the portfolio applications.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'portfolio',
    'services',
]

# Define the middleware stack used by Django for each request.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Tell Django where the main URL configuration lives.
ROOT_URLCONF = 'core.urls'

# Configure Django's template engine and the shared templates folder.
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

# Define the WSGI entry point used by deployment servers.
WSGI_APPLICATION = 'core.wsgi.application'

# Use SQLite for this portfolio project because it is simple for local development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Keep Django's standard password validators enabled.
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Set the language used by the project.
LANGUAGE_CODE = 'en-us'

# Set the local development time zone.
TIME_ZONE = 'Africa/Dar_es_Salaam'

# Enable Django's internationalization support.
USE_I18N = True

# Enable timezone-aware date and time values.
USE_TZ = True

# Tell Django that static files are served from the /static/ URL.
STATIC_URL = 'static/'

# Tell Django where the project's custom static files are stored.
STATICFILES_DIRS = [BASE_DIR / 'static']

# Tell Django where uploaded media files are stored.
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Use Django's recommended automatic primary-key type.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ---------------------------------------------------------
# EMAIL CONFIGURATION
# ---------------------------------------------------------

# Tell Django to use Gmail's SMTP server to send emails.
EMAIL_HOST = 'smtp.gmail.com'

# Gmail SMTP uses port 587 for secure TLS connections.
EMAIL_PORT = 587

# Tell Django to use TLS encryption when connecting to Gmail.
EMAIL_USE_TLS = True

# Your Gmail address that will send the portfolio emails.
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")

# IMPORTANT:
# This must be a Google App Password, NOT your normal Gmail password.
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")

# Email address that Django uses as the sender.
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER