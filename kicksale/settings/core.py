import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%furs7kn$f2q5e6hl&rgj4hv-a!xo-ou#lqo0s85pd%sarxo0l'

#TODO: #6
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'testkicksale2.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'store_cart',
    'account',
    'crispy_forms',
    'payment',
    'orders',
    'mptt',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kicksale.urls'

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
                'store.context_processors.categories_all',
                'store_cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'kicksale.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'daki474lll30rf',
        'USER': 'grzjjkjvfambgn',
        'PASSWORD': '96c34a922a476158515609582a9a0ac619c975c85a1d502ac3b8e1a4c4ce7a28',
        'HOST': 'ec2-34-235-31-124.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Canada/Mountain'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Cart session ID
CART_SESSION_ID = 'cart'

##TODO: #6 Point to prod server insted of local! 
# && not using OS? (win & macos issues?)
MEDIA_URL = '/static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/static/media/')

# Customer user model
AUTH_USER_MODEL = 'account.UserBase'
LOGIN_REDIRECT_URL = '/account/dashboard'
LOGIN_URL = '/account/login/'

# Django Crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'canadakicksale@gmail.com'
EMAIL_HOST_PASSWORD = 'dyucnyihvezqcoea'
EMAIL_PORT = 587

# Stripe
os.environ.setdefault('STRIPE_PUBLISHABLE_KEY', 'pk_test_51LMbCrBlqtly1GXPvOkGJmRnUQdU6foSK6Z0IqDSCn67bVco5I01IygbPZCMSQJpgucn9lHD5aywAwF0JXTcQ8TO00fc5ho7Rw')
STRIPE_SECRET_KEY = 'sk_test_51LMbCrBlqtly1GXPi93EUJ84iTmWmYrWtWrOmaW28uYvC0VEnnYEo3DnOrMH64phLFG1SsdXUIZFnYgH7qLLmiNo00WHYW5gCw'
STRIPE_ENDPOINT_SECRET = 'whsec_2545501c69a4a5f431c9bd1fedb887bc874943db594049c9c6aad06e2ff94c92'

# security.W018
DEBUG = False

# security.W016
CSRF_COOKIE_SECURE = True

# security.W012
SESSION_COOKIE_SECURE = True

# security.W008
SECURE_SSL_REDIRECT = True

# security.W004
SECURE_HSTS_SECONDS = 31536000 # One year in seconds

# Another security settings
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True