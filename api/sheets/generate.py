from django.conf import settings
from typing import List
from product.models import Product
from order.models import Order
from django.db.models import QuerySet
from sheets.input_cleansing import zero_product_count
import pandas as pd
import xlsxwriter

class InputSheet:
    '''Responsible for generating the Input sheet from Orders.'''
    _customer_headers = []
    _product_headers = []
    _product_ids = []
    _cols = []


    @property
    def headers(self):
        headers = []
        headers = [self._customer_headers + self._product_headers]
        return headers

    @property
    def customer_headers(self) -> List:
        self._customer_headers = []
        fields = settings.INPUT_SHEET.get('ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS',[])
        for h in fields:
            self._customer_headers.append(Order._meta.get_field(h).verbose_name)

        return self._customer_headers

    @property
    def product_ids(self) -> List:
        return self._product_ids

    @property
    def product_headers(self) -> List:
        self._product_headers = []
        qs = Product.objects.filter(published=True)
        product_names = list(qs.values_list('name', flat=True))
        product_ids = list(qs.values_list('id', flat=True))
        ids_names = list(qs.values('id','name'))
        self._product_headers = [ p.get('name') for p in ids_names]
        self._product_ids = [ p.get('id') for p in ids_names]
        return self._product_headers

    def order_cols(self, f_event_id:int, orders:QuerySet=None):
        self._cols,cols = [],[]
        if not orders:
            orders = Order.objects.filter(fulfillment_event_id=f_event_id)
        fields = orders.values_list(*settings.INPUT_SHEET.get('ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS',[]))

        for cust_order_fields,obj in zip(fields,orders):
            customer_order_product_counts = tuple(
                [zero_product_count(obj.product_count(p_id)) for p_id in self._product_ids])
            cols.append(cust_order_fields + customer_order_product_counts)

        self._cols = cols
        return self._cols

    def prepare(self, f_event_id:int):
        self.customer_headers
        self.product_headers
        self.order_cols(f_event_id)

    def to_df(self, f_event_id:int):
        self.prepare(f_event_id)
        df = pd.DataFrame(self.headers + self._cols)
        output = df.transpose()

        return output

    def save_xlsx(self, f_event_id:int, path='./generated_input.xlsx'):
        df_output = self.to_df(f_event_id)

        writer = pd.ExcelWriter(path, engine='xlsxwriter')
        sheet_name=f'{INPUT-dd-mm-yy}'
        df_output.to_excel(writer, sheet_name=sheet_name)

        workbook = writer.book
        worksheet = writer.sheets[sheet_name]
        worksheet.set_zoom(60)
        # Add a format. Green fill with dark green text.
        format2 = workbook.add_format({'bg_color': '#C6EFCE',
                                    'font_color': '#006100'})
        writer.save()
