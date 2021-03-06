import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)


SECRET_KEY = os.environ.get("SECRET_KEY", "change_for_env")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", " ").split(" ")


# Application definition

INSTALLED_APPS = [
    # third party libraries
    "graphene_django",
    "djmoney",
    "django_extensions",
    "adminsortable2",
    # user apps
    "shared",
    "product",
    "order",
    "sheets",
    "cloudstore",
    "customer",
    "snapshot",
    # moved django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "farmbox.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "farmbox.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


DATABASE_HOSTS = {"STAGING": "ec2-176-34-123-50.eu-west-1.compute.amazonaws.com"}

DB_NAME = os.getenv("DB_NAME")
DATABASES = {
    "postgres": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": DATABASE_HOSTS["STAGING"],
        "PORT": os.getenv("DB_PORT", "5432"),
    },
    "sqlite": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/


STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")


FARMBOX_DROPBOX_ACCESS_TOKEN = os.environ.get("FARMBOX_DROPBOX_ACCESS_TOKEN", "")

DEFAULT_SUPERUSER = {
    "username": "admin",
    "email": os.environ.get("DEFAULT_SUPERUSER_EMAIL", "dev@howapped.com"),
    "password": os.environ.get("DEFAULT_SUPERUSER_PASSWORD"),
}
NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER = 5
FULFILLMENT_METHODS_DELIVERY = "Delivery"
FULFILLMENT_METHODS_COLLECTION_OCKLEY = "Collect from Ockley Shop"
FULFILLMENT_METHODS_COLLECTION_DENBIES = "Collect from Denbies Shop"

COLLECTION_LOCATIONS_DENBIES = "Denbies"
COLLECTION_LOCATIONS_OCKLEY = "Ockley"

DEFAULT_CURRENCY = "GBP"

GRAPHENE = {"SCHEMA": "farmbox.schema.schema"}

DISPLAY_DATE_FORMAT = "%a %d/%m/%Y"
# DATE_FORMAT = "%a %d/%m/%Y"
PRODUCT_CATEGORIES_VEGBAG = "Vegbag"
PRODUCT_CATEGORIES_ITEM = "Item"

PRODUCT_PICKING_PACKING_SURCHARGE = {
    PRODUCT_CATEGORIES_VEGBAG: [],
    PRODUCT_CATEGORIES_ITEM: [
        {
            "fulfillment_method": FULFILLMENT_METHODS_DELIVERY,
            "grand_total_condition": ["<", 10],
            "surcharge": 1,
        },
        {
            "fulfillment_method": FULFILLMENT_METHODS_DELIVERY,
            "grand_total_condition": [">", 10],
            "surcharge": 2,
        },
        {
            "fulfillment_method": FULFILLMENT_METHODS_COLLECTION_DENBIES,
            "grand_total_condition": ["<", 10],
            "surcharge": 1,
        },
    ],
}

# only applied once to subtotal
PICKING_PACKING_SURCHARGE = {
    PRODUCT_CATEGORIES_VEGBAG: [
        {"fulfillment_method": FULFILLMENT_METHODS_DELIVERY, "surcharge": 2},
    ],
    PRODUCT_CATEGORIES_ITEM: [
        {
            "fulfillment_method": FULFILLMENT_METHODS_DELIVERY,
            "grand_total_condition": ["<", 10],
            "surcharge": 2,
        },
        {
            "fulfillment_method": FULFILLMENT_METHODS_DELIVERY,
            "grand_total_condition": [">", 10],
            "surcharge": 2,
        },
        {
            "fulfillment_method": FULFILLMENT_METHODS_COLLECTION_DENBIES,
            "grand_total_condition": ["<", 10],
            "surcharge": 1,
        },
    ],
}

INPUT_SHEET = {
    "ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS": [
        "f_number",
        "customer_first_name",
        "customer_last_name",
        "customer_address",
        "customer_postcode",
        "customer_email",
        "customer_phone",
        "fulfillment_method",
        "collection_location",
        "notes",
    ]
}

CUSTOMER_SHEET = {
    "ORDER_FIELDS": (
        "f_number",
        "customer_first_name",
        "customer_last_name",
        "customer_postcode",
        "customer_address",
        "fulfillment_method",
        "fulfillment_event",
    )
}

CUSTOMER_SHEETS_DIR = "customer-sheets"
CUSTOMER_SHEETS_PATH = os.path.join(MEDIA_ROOT, CUSTOMER_SHEETS_DIR)

ORDER_SHEET = {
    "PRODUCT_NAME_COL": "A",
    "PRODUCT_COUNT_COL": "C",
    "PRODUCT_PRICE_COL": "D",
    "DETAILS_CELL_MAP": {
        "C1": "customer_first_name",
        "C2": "customer_last_name",
        "C3": "customer_address",
        "C4": "customer_postcode",
        "C5": "customer_email",
        "C6": "customer_phone",
        "C7": "fulfillment_method",
        "C8": "collection_location",
        "C9": "fulfillment_event__target_date",
    },
}

SAMPLE_ORDER_SHEET_DIR = os.path.join(PROJECT_DIR, "order", "sample_sheets")
SAMPLE_ORDER_SHEET_PATH = os.path.join(SAMPLE_ORDER_SHEET_DIR, "current.xlsx")
LOCAL_FETCH_SHEETS_DIR = os.path.join(SAMPLE_ORDER_SHEET_DIR, "local_fetch")

SAMPLE_PRODUCT_SHEET_DIR = os.path.join(PROJECT_DIR, "product", "sample_sheets")
LOCAL_FETCH_PRODUCT_SHEETS_DIR = os.path.join(SAMPLE_PRODUCT_SHEET_DIR, "local_fetch")


# Cloud store
# Remote folder names
NEW_ORDERS_FOLDER = "new-orders"
NEW_PRODUCTS_FOLDER = "new-products"
PROCESSED_ORDERS_FOLDER = "processed-orders"
PROCESSED_PRODUCTS_FOLDER = "processed-products"
BACKUP_DB_FOLDER = "backup-db"
DEBUG_FOLDER = "howapped-debug"
CLOUD_SUBFOLDERS = (
    BACKUP_DB_FOLDER,
    DEBUG_FOLDER,
    NEW_ORDERS_FOLDER,
    PROCESSED_ORDERS_FOLDER,
    NEW_PRODUCTS_FOLDER,
    PROCESSED_PRODUCTS_FOLDER,
)
TESTING_DIRNAME = "testing"
NEW_ORDERS_REMOTE_PATH = f"/{NEW_ORDERS_FOLDER}"
NEW_PRODUCTS_REMOTE_PATH = f"/{NEW_PRODUCTS_FOLDER}"
TESTING_ORDERS_REMOTE_PATH = f"/{os.path.join(NEW_ORDERS_FOLDER,TESTING_DIRNAME)}"

BACKUP_DB_BEFORE_PRODUCT_IMPORT = False
