import pytest
import os
from django.conf import settings
from datetime import datetime
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader

FILENAME = os.path.basename(settings.SAMPLE_ORDER_SHEET_PATH)


@pytest.mark.django_db
def test_a_new_customer_will_get_stored_keyed_by_email_address():

    expected_actual = (
        ("customer_first_name", "Nigel"),
        ("customer_last_name", "Samplestock"),
        ("customer_address", "107, Fairfield Drive"),
        ("customer_postcode", "rh4 1jj"),
        ("customer_email", "Dev+farmbox99@howapped.com"),
        ("customer_phone", "0789 449 542"),
        ("fulfillment_method", "Collect from Denbies Shop"),
        ("fulfillment_event__target_date", datetime(2020, 5, 12, 0, 0)),
    )
    expected_actual = dict((x, y) for x, y in expected_actual)
    r = OrderSheetReader()
    xlsx_file = os.path.join(settings.SAMPLE_ORDER_SHEET_DIR, FILENAME)
    r.read_to_model(xlsx_file)

    customer = r.customer.__dict__
    indexes = [
        "first_name",
        "last_name",
        "address",
        "postcode",
        "postcode",
        "email",
        "phone",
    ]
    for i in indexes:
        assert expected_actual.get(f"customer_{i}") == customer.get(i)
