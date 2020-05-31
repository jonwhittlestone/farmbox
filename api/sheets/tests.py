import pytest
import os
from datetime import datetime
from datetime import date
from django.conf import settings
from order.models import FulfillmentEvent
from order.models import FulfillmentEvent
from product.models import Product
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader

def test_collect_files():
    xlsx_files = collect_files_for_reading()
    assert type(xlsx_files) == list
    assert len(xlsx_files) > 0


@pytest.mark.django_db
def test_first_cell_in_sample_order_form_is_read_by_openpyxl():
    r = OrderSheetReader()
    excel_data = r.read()
    assert str(type(r.excel_data[0][0])) == "<class 'openpyxl.cell.read_only.ReadOnlyCell'>"


@pytest.mark.django_db
def test_order_details_are_captured_to_instance_variable():
    expected_actual = (
        ('customer_first_name','Nigel'),
        ('customer_last_name','Samplestock'),
        ('customer_address', '107, Fairfield Drive'),
        ('customer_postcode','rh4 1jj'),
        ('customer_email','Dev+farmbox99@howapped.com'),
        ('customer_phone','0789 449 542'),
        ('fulfillment_method','Collect from Denbies Shop'),
        ('fulfillment_event__target_date', datetime(2020,5,12,0,0))
    )
    r = OrderSheetReader()
    excel_data = r.read(os.path.join(settings.SAMPLE_ORDER_SHEET_DIR,'current.xlsx'))
    actual = r.order_details
    for expected_idx,expected in expected_actual:
        assert actual.get(expected_idx,'') == expected

@pytest.mark.django_db
@pytest.mark.skip(reason="Only for real-world debugging on local")
def test_i_can_read_a_locally_stored_sheet_to_an_order():

    r = OrderSheetReader()
    filename = 'Garrood 2.xlsx'
    path = os.path.join(settings.LOCAL_FETCH_SHEETS_DIR,filename)

    excel_data = r.read(path)

    order_details = r.order_details
    assert True


@pytest.mark.django_db
def test_order_sheet_products_count():
    expected = {
        'Butternut Squash FV0013' : 1,
    }
    # product names
    products = list(Product.objects.values_list('name', flat=True))
    r = OrderSheetReader()
    r.read()
    actual = r.product_counts
    for exp_p_name, exp_count in expected.items():
        if exp_p_name in list(actual.keys()):
            assert exp_count == actual.get(exp_p_name)

    # loop through actual, where product counts are None, assert that an entry does not exist in expected
    for actual_p_name, count in actual.items():
        if count == None:
            found = [p_name for p_name,count in expected.items() if actual_p_name == p_name]
            if len(found) > 0:
                assert False


@pytest.mark.django_db
def test_create_a_new_fulfillment_event_from_order_sheet():
    mocked_date_in_order_details = {
        # openpxyl returns a datetime.datetime vs. target_date field is datetime.date
        'fulfillment_event__target_date': datetime(2020,12,1,0,0)
    }
    r = OrderSheetReader()
    # scenario 1: There are no fevents in DB, so create one for the mocked event
    r.read()
    f_event = r.get_or_create_fulfillment_event(mocked_date_in_order_details)
    f_event_target_date_to_dt = datetime.combine(f_event.target_date, datetime.min.time())
    assert f_event_target_date_to_dt == mocked_date_in_order_details.get(
        'fulfillment_event__target_date')
