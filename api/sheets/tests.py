import pytest
from datetime import datetime
from product.models import Product
from sheets.reader import collect_files_for_reading, OrderSheet as OrderSheetReader

def test_collect_files():
    xlsx_files = collect_files_for_reading()
    assert type(xlsx_files) == list
    assert len(xlsx_files) > 0

def test_first_cell_in_sample_order_form_is_read_by_openpyxl():
    r = OrderSheetReader()
    excel_data = r.read()
    assert str(type(r.excel_data[0][0])) == "<class 'openpyxl.cell.read_only.ReadOnlyCell'>"

def test_order_details_are_captured_to_instance_variable():
    expected_actual = (
        ('customer_name','Nigel Samplestock'),
        ('customer_address', '107, Fairfield Drive'),
        ('customer_postcode','rh4 1jj'),
        ('customer_email','Dev+farmbox99@howapped.com'),
        ('customer_phone','0789 449 542'),
        ('fulfillment_method','Collection'),
        ('collection_location','Denbies'),
        ('fulfillment_event__target_date', datetime(2020,4,24,0,0))
    )
    r = OrderSheetReader()
    excel_data = r.read()
    expected = r.order_details
    for expected_idx,actual in expected_actual:
        assert expected.get(expected_idx,'') == actual


@pytest.mark.django_db
def test_order_sheet_products_count():
    expected = {
        'Village Greens Veg Bag : Large' : 1,
        'Butternut Squash' : 1,
        'Avocado : Ripe ready to eat': 1,
        'Lettuce :Romaine':1,
        'Lemon': 1,
        'Raspberries':1,
        'Strawberries':2,
        '1 L Skimmed': 1 
    }
    # product names
    products = list(Product.objects.values_list('name', flat=True))
    r = OrderSheetReader()
    r.read()
    actual = r.product_counts
    for exp_p_name, exp_count in expected.items():
        if exp_p_name in list(actual.keys()):
            debug = True
            assert exp_count == actual.get(exp_p_name)
    
    # loop through actual, where product counts are None, assert that an entry does not exist in expected
    for actual_p_name, count in actual.items():
        if count == None:
            found = [p_name for p_name,count in expected.items() if actual_p_name == p_name]
            if len(found) > 0:
                assert False


