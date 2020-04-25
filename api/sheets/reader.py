import os
import json
from pathlib import Path
import sys
from openpyxl import load_workbook
from product.models import Product
from order.models import OrderForm
from django.conf import settings
from sheets.input_cleansing import OrderSheet as OrderSheetCleanser

FILENAME = 'sample-order-v070420.xlsx'

def collect_files_for_reading(path = None) -> list:
    if not path:
        path = os.path.join(settings.PROJECT_DIR,'order')
        xlsx_files = Path(path).glob("*.xlsx")
    return list(xlsx_files)

class OrderSheet():
    excel_data: []
    mdl: OrderForm
    cell_cleanser: OrderSheetCleanser 
    _order_details: {}
    _product_counts: {}

    def __init__(self):
        self.cell_cleanser = OrderSheetCleanser()


    def read(self):
        xlsx_file = os.path.join(settings.PROJECT_DIR,'order',FILENAME)
        workbook = load_workbook(filename=xlsx_file, read_only=True)
        worksheet = workbook.active
        self.excel_data = list(worksheet.rows)
        return self.excel_data
    
    @property
    def order_details(self):
        self._order_details = {}
        cell_map = settings.ORDER_SHEET.get('DETAILS_CELL_MAP',{})
        # self._order_details = ret
        for row in self.excel_data:
            for cell in row:
                try:
                    self._order_details[cell_map.get(cell.coordinate,'')] = cell.internal_value
                except Exception as e:
                    pass
        del self._order_details['']
        return self._order_details
    
    @property
    def product_counts(self):
        self._product_counts = {}

        # product names
        products = list(Product.objects.values_list('name', flat=True))
        products_rows = []

        # first pass to capture all cell.row where there are valid products
        for row in self.excel_data:
            for cell in row:
                if cell.value == None:
                    break
                if cell.column_letter == settings.ORDER_SHEET.get('PRODUCT_NAME_COL', '') and cell.internal_value in products:
                    products_rows.append(row)
        
        for row in products_rows:
            for cell in row:
                if cell.column_letter == settings.ORDER_SHEET.get('PRODUCT_NAME_COL'):
                    key = cell.internal_value
                if cell.column_letter == settings.ORDER_SHEET.get('PRODUCT_COUNT_COL'):
                    value = self.cell_cleanser.product_count(
                        cell.internal_value)
                    # value = cell.internal_value
            try:
                self._product_counts[key] = value
            except Exception as e:
                break
        return self._product_counts
