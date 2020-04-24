import os
import json
from pathlib import Path
import sys
from openpyxl import load_workbook
from django.conf import settings

FILENAME = 'sample-order-v070420.xlsx'

def collect_files_for_reading(path = None) -> list:
    if not path:
        path = os.path.join(settings.PROJECT_DIR,'order')
        xlsx_files = Path(path).glob("*.xlsx")
    return list(xlsx_files)

class OrderSheet():
    excel_data: []
    _order_details: {}

    def read(self):
        xlsx_file = os.path.join(settings.PROJECT_DIR,'order',FILENAME)
        workbook = load_workbook(filename=xlsx_file, read_only=True)
        worksheet = workbook.active
        self.excel_data = list(worksheet.rows)
        return self.excel_data
    
    @property
    def order_details(self):
        ret = {'customer_name':'Nigel Samplestock'}
        # cell_map = settings.ORDER_SHEET.get('DETAILS_CELL_MAP',{})
        self._order_details = ret
        return ret