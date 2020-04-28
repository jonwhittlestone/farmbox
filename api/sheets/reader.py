import os
import json
import sys
from pathlib import Path
from django.utils import timezone
from openpyxl import load_workbook
from product.models import Product
from order.models import OrderForm, FulfillmentEvent, Order, ProductQuantity
from django.conf import settings
from sheets.input_cleansing import OrderSheet as OrderSheetCleanser

FILENAME = 'sample-order-v070420.xlsx'

def collect_files_for_reading(path = None) -> list:
    if not path:
        path = os.path.join(settings.PROJECT_DIR,'order')
    xlsx_files = Path(path).glob("*.xlsx")
    return list(xlsx_files)

class OrderSheet():
    filename: str
    excel_data: []
    _order: Order
    obj: OrderForm
    cell_cleanser: OrderSheetCleanser 
    _order_details: {}
    _product_counts: {}

    def __init__(self):
        self.cell_cleanser = OrderSheetCleanser()

    def create_order(self, f_event:FulfillmentEvent, order_details = None, product_counts = None):
        '''Creates the order and then adds the products'''
        if not order_details:
            order_details = self._order_details
        if not product_counts:
            product_counts = self._product_counts

        del order_details['fulfillment_event__target_date']
        order_details['fulfillment_event_id'] =  f_event.id
        order_details['created_at'] = timezone.now()
        order_details['modified_at'] = timezone.now()
        self._order = Order.objects.create(**order_details)
        for p_name, count in product_counts.items():
            if count != None:
                p = Product.objects.filter(name=p_name).first()
                ProductQuantity.objects.create(order=self._order, product=p, quantity=count)
        return self._order

    def read_to_model(self, file = None) -> Order:
        '''Creates an Order model instance from an Order Sheet.'''
        self.read(file)
        self.order_details
        self.product_counts
        f_event = self.get_or_create_fulfillment_event()
        self.create_order(f_event)
        return self._order

    def get_or_create_fulfillment_event(self, order_details = None):
        '''
            Given parsed target_date, use existing f_event, or if date
            does not exist, create new model instance with that target_date
        '''
        if not order_details:
            order_details = self._order_details
        converted_date = order_details.get('fulfillment_event__target_date').date()
        f_event_obj, created = FulfillmentEvent.objects.get_or_create(target_date=converted_date)
        f_event_obj.target_date = converted_date
        f_event_obj.save()

        self.obj.fulfillment_event = f_event_obj
        return f_event_obj

    def read(self, xlsx_file = None):
        if not xlsx_file:
            xlsx_file = os.path.join(settings.PROJECT_DIR,'order',FILENAME)
        self.obj = OrderForm.objects.create(filename=xlsx_file, created_at=timezone.now())
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
