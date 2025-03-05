from MySite.settings import *
# PRODUCTION SETTING

# DEVELOPMENT SETTING

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a!id*ofr4c#f9o(bd95eu+!+w7bc3%7jzh&3hnz_t=5wm*b$pw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# sites framework
SITE_ID = 2

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#static and media root
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [ 
    BASE_DIR / "static",
     ]



# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True