"""
Django settings for farmbox project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r%kt5z+g%(zwz8t2(hu5k=4hj74-tcwluanc0n6q9%6)fm6hzu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third party libraries
    'graphene_django',
    'djmoney',
    'django_extensions',

    # user apps
    'shared',
    'order',
    'product',
    'sheets'
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

ROOT_URLCONF = 'farmbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [            
            # os.path.join(PROJECT_DIR, 'templates'),
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

WSGI_APPLICATION = 'farmbox.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

DEFAULT_SUPERUSER = {
    'username': 'admin',
    'email': 'dev@howapped.com',
    'password': 'Evoke-Enduring8-Figurine'
}

FULFILLMENT_METHODS_DELIVERY = 'Delivery'
FULFILLMENT_METHODS_COLLECTION = 'Collection'

COLLECTION_LOCATIONS_DENBIES = 'Denbies'
COLLECTION_LOCATIONS_OCKLEY = 'Ockley'

DEFAULT_CURRENCY = 'GBP'

GRAPHENE = {
    'SCHEMA': 'farmbox.schema.schema'
}

DISPLAY_DATE_FORMAT = "%a %d/%m/%Y"
PRODUCT_CATEGORIES_VEGBAG = 'Vegbag'
PRODUCT_CATEGORIES_ITEM = 'Item'

PRODUCT_PICKING_PACKING_SURCHARGE = {
    PRODUCT_CATEGORIES_VEGBAG: [],
    PRODUCT_CATEGORIES_ITEM:[
        {'fulfillment_method': FULFILLMENT_METHODS_DELIVERY,'grand_total_condition':['<',10],'surcharge':1},
        {'fulfillment_method': FULFILLMENT_METHODS_DELIVERY,'grand_total_condition':['>',10], 'surcharge':2},
        {'fulfillment_method': FULFILLMENT_METHODS_COLLECTION,'grand_total_condition':['<',10], 'surcharge':1},
    ]
}

# only applied once to subtotal
PICKING_PACKING_SURCHARGE = {
    PRODUCT_CATEGORIES_VEGBAG: [
        {'fulfillment_method': FULFILLMENT_METHODS_DELIVERY,'surcharge':2},
    ],
    PRODUCT_CATEGORIES_ITEM:[
        {'fulfillment_method': FULFILLMENT_METHODS_DELIVERY,'grand_total_condition':['<',10], 'surcharge':2},
        {'fulfillment_method': FULFILLMENT_METHODS_DELIVERY,'grand_total_condition':['>',10], 'surcharge':2},
        {'fulfillment_method': FULFILLMENT_METHODS_COLLECTION,'grand_total_condition':['<',10], 'surcharge':1},
    ]
}

INPUT_SHEET = {
    'ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS': [
        'customer_name', 'customer_address', 'customer_postcode', 
        'customer_email', 'customer_phone', 
        'fulfillment_method', 'collection_location', 'notes'
    ]
}
