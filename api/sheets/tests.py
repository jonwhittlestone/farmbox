import pytest
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
    r = OrderSheetReader()
    excel_data = r.read()

    assert r.order_details.get('customer_name','') == 'Nigel Samplestock'
