from .base import BASE_DIR
from .bas import *
import os


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    },
}


# test variable to identify if this env file is used at runtime
ENV = "prod"

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://ad8f8ff44e804b90835d6c3a63d02ef8@o389188.ingest.sentry.io/5227023",
    integrations=[DjangoIntegration()],
    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,
)
