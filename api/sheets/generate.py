from django.conf import settings
from typing import List
from product.models import Product
from order.models import Order
from django.db.models import QuerySet
from sheets.input_cleansing import zero_product_count
import pandas as pd
import xlsxwriter

class CustomerSheet:
    '''Responsible for generating a customer sheet for an order.'''

    _customer_headers: []
    _product_headers: []
    order: Order

    def __init__(self, order:Order):
        self.order = order

    @property
    def customer_headers(self) -> tuple:
        return settings.CUSTOMER_SHEET['CUSTOMER_HEADERS']

    @property
    def product_headers(self) -> tuple:
        product_names = list(self.order.products.values_list('name',flat=True))
        return tuple(product_names)

    @property
    def headers(self) -> tuple:
        '''Sheet vertical column of headers comprising Order details and product names'''
        SPACER = ('',)
        TOTAL_HEADER = ('TOTAL',)
        headers = (self.customer_headers + SPACER + self.product_headers + TOTAL_HEADER)
        return headers

    @property
    def pack_sizes(self) -> tuple:
        '''Horizontal row of packsizes'''
        return ('','','','','','','','Std Pack Size', '1','1','1',''),


    def to_df(self):
        df = pd.DataFrame([
            self.headers,
            # Pack size row
            self.pack_sizes,
            # Current Price row
            ('','','','','','','','Current Price', '£1.00','£1.30','£11.00',''),
            ('20-1-001','Jon','Whittler','92, Long Acre, Dorking. Surrey.','RH4 1LD','DELIVERY','Fri 8 Jun 2020','Quantity', '1','2','1','5'),
            # Pad out rows to force next output to new page
            ('','','','','','', '','Cost','£1.00','£2.60','£11.00','£14.60'),
            ('','','','','','', '','','','','',''),
            ('','','','','','', '','','','','',''),
            ('','','','','','', '','','','','',''),
            ('','','','','','', '','','','','',''),
        ])
        df_transposed = df.transpose()
        return df_transposed



class InputSheet:
    '''Generating the Input sheet from Orders.'''
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
        self._product_headers, self._product_ids = Product.published_names()
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
