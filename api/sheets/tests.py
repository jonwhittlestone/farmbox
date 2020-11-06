import pytest
import os
from datetime import datetime, date
from decimal import Decimal
from django.conf import settings
from order.models import FulfillmentEvent
from product.models import Product
from sheets.reader import (
    collect_files_for_reading,
    OrderSheet as OrderSheetReader,
    ProductSelectionSheet as ProductSheetReader,
)


def test_collect_files():
    xlsx_files = collect_files_for_reading()
    assert type(xlsx_files) == list
    assert len(xlsx_files) > 0


@pytest.mark.django_db
def test_first_cell_in_sample_order_form_is_read_by_openpyxl():
    r = OrderSheetReader()
    r.read()
    assert (
        str(type(r.excel_data[0][0]))
        == "<class 'openpyxl.cell.read_only.ReadOnlyCell'>"
    )


class TestDetailsAreCaptured:
    @pytest.mark.django_db
    def test_product_details_are_captured_to_reader_instance_variable(self):
        """
        Matching with expected from sample product selection
        sheet at
        `api/product/sample_sheets/product_selection_fetch_example.xlsx`
        """
        expected = [
            {
                "name": "Village Greens Veg Bag : Large FV3355",
                "code": "FV3355",
                "price": Decimal(15.00),
            },
            {
                "name": "Village Greens Veg Bag - Medium  FV0083",
                "code": "FV0083",
                "price": Decimal(13.00),
            },
            {
                "name": "Village Greens Veg Bag : Small FV3354",
                "code": "FV3354",
                "price": Decimal(11.00),
            },
            {
                "name": "Aubergine FV0009",
                "code": "FV0009",
                "price": Decimal(1.30),
            },
            {
                "name": "Sweet Potato FV0035",
                "code": "FV0035",
                "price": Decimal(1.10),
            },
            {
                "name": "Avocado : Ripe ready to eat FV0094",
                "code": "FV0094",
                "price": Decimal(1.55),
            },
            {
                "name": "Strawberries FV0065",
                "code": "FV0065",
                "price": Decimal(8.00),
            },
            {
                "name": "1 Pint Full Fat : Aldhurst Farm MI5020",
                "code": "MI5020",
                "price": Decimal(1.10),
            },
            {
                "name": "1 Pint Skimmed MI1027",
                "code": "MI1027",
                "price": Decimal(0.8),
            },
            {
                "name": "Chalk Hills Bloomer BR2291",
                "code": "BR2291",
                "price": Decimal(2.10),
            },
            {
                "name": "Coffee Real Beans SZ9006",
                "code": "SZ9006",
                "price": Decimal(6.15),
            },
            {
                "name": "Tea Bags : Clipper Everyday x 80 (Organic) SZ0823",
                "code": "SZ0823",
                "price": Decimal(2.50),
            },
            {
                "name": "Hepworth Blonde Lager 500ml  (Organic, GF, Vegan) ST0327",
                "code": "ST0327",
                "price": Decimal(2.95),
            },
        ]

        r = ProductSheetReader()
        filename = "product_selection_fetch_example.xlsx"
        r.read(os.path.join(settings.SAMPLE_PRODUCT_SHEET_DIR, filename))
        actual = r.product_details
        for i, exp in enumerate(expected):
            assert actual[i].get("name") == expected[i].get("name")
            assert actual[i].get("code") == expected[i].get("code")
            assert actual[i].get("price") == expected[i].get("price")

    @pytest.mark.django_db
    def test_order_details_are_captured_to_instance_variable(self):
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
        r = OrderSheetReader()
        r.read(os.path.join(settings.SAMPLE_ORDER_SHEET_DIR, "current.xlsx"))
        actual = r.order_details
        for expected_idx, expected in expected_actual:
            assert actual.get(expected_idx, "") == expected


@pytest.mark.django_db
@pytest.mark.skip(reason="Only for real-world debugging on local")
def test_i_can_read_a_locally_stored_sheet_to_an_order():
    r = OrderSheetReader()
    filename = "Garrood 2.xlsx"
    path = os.path.join(settings.LOCAL_FETCH_SHEETS_DIR, filename)
    r.read(path)
    r.order_details
    pass


@pytest.mark.django_db
def test_order_sheet_products_count():
    expected = {
        "Butternut Squash FV0013": 1,
    }
    r = OrderSheetReader()
    r.read()
    actual = r.product_counts
    for exp_p_name, exp_count in expected.items():
        if exp_p_name in list(actual.keys()):
            assert exp_count == actual.get(exp_p_name)

    # loop through actual, where product counts are None, assert that an entry does not exist in expected
    for actual_p_name, count in actual.items():
        if count is None:
            found = [
                p_name for p_name, count in expected.items() if actual_p_name == p_name
            ]
            if found is None:
                assert False


@pytest.mark.django_db
def test_create_a_new_fulfillment_event_from_order_sheet():
    mocked_date_in_order_details = {
        # openpxyl returns a datetime.datetime vs. target_date field is datetime.date
        "fulfillment_event__target_date": datetime(2020, 12, 1, 0, 0)
    }
    r = OrderSheetReader()
    # scenario 1: There are no fevents in DB, so create one for the mocked event
    r.read()
    f_event = r.get_or_create_fulfillment_event(mocked_date_in_order_details)
    f_event_target_date_to_dt = datetime.combine(
        f_event.target_date, datetime.min.time()
    )
    assert f_event_target_date_to_dt == mocked_date_in_order_details.get(
        "fulfillment_event__target_date"
    )
