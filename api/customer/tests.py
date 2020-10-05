import pytest
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader


@pytest.mark.django_db
def test_a_new_customer_will_get_stored_keyed_by_email_address():

    assert True


def test_an_existing_customer_will_get_saved_to_an_order_keyed_by_email_address():

    assert True
