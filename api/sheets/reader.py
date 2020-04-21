import os
import json
from pathlib import Path
import sys
from openpyxl import load_workbook
from django.conf import settings

FILENAME = 'sample-order-v070420.xlsx'

class OrderSheet():

    def read(self):
        xlsx_file = os.path.join(settings.PROJECT_DIR,'order',FILENAME)
        workbook = load_workbook(filename=xlsx_file, read_only=True)
        worksheet = workbook.active
        excel_data = list(worksheet.rows)
        debug=True