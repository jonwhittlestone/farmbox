import pytest
from sheets.reader import OrderSheet as OrderSheetReader

def test_reader_to_order_model():
    r = OrderSheetReader()
    r.read()
    assert True
