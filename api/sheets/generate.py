from django.conf import settings
from typing import List
from product.models import Product
from order.models import Order
from django.db.models import QuerySet
from sheets.input_cleansing import zero_product_count
import pandas as pd
import xlsxwriter

SPACER = ('',)
class CustomerSheet:
    '''Responsible for generating a customer sheet for an order.'''

    _customer_headers: []
    _product_headers: []
    totals: {}
    order: Order

    def __init__(self, order:Order):
        self.order = order
        self.totals = {'quantity':0}

    @property
    def customer_headers(self) -> tuple:
        fields = settings.CUSTOMER_SHEET['ORDER_FIELDS'][0:-1]
        field_names = [self.order._meta.get_field(
            f).verbose_name for f in fields]
        field_names.append('Event Date')
        return tuple(field_names)

    @property
    def product_headers(self) -> tuple:
        product_names = list(self.order.products.values_list('name',flat=True))
        return tuple(product_names)

    @property
    def headers(self) -> tuple:
        '''Sheet vertical column of headers comprising Order details and product names'''
        TOTAL_HEADER = ('TOTAL',)
        headers = (self.customer_headers + SPACER + self.product_headers + TOTAL_HEADER)
        return headers

    @property
    def pack_sizes(self) -> tuple:
        '''vertical column of packsizes'''
        pack_sizes_empty_cells = (SPACER * len(self.customer_headers))
        pack_sizes = tuple(self.order.products.values_list('pack_size',flat=True))
        return  pack_sizes_empty_cells + ('Std Pack Size',) + pack_sizes + SPACER

    @property
    def product_prices(self) -> tuple:
        '''Vertical column of product prices (with the header)'''
        product_prices_empty_cells = (SPACER * len(self.customer_headers))
        product_prices = tuple(self.order.products.values_list('price',flat=True))
        return product_prices_empty_cells + ('Current Price',) + product_prices + SPACER

    @property
    def order_details(self):
        '''Vertical column that consists of order details, and quantities.'''
        HEADER = 'Quantity'
        self.totals['quantity'] = sum(self.product_quantities)
        details = (self.customer_details + (HEADER,) + self.product_quantities + (self.totals['quantity'],))
        return details

    @property
    def customer_details(self) -> tuple:
        return tuple([getattr(self.order,f) for f in settings.CUSTOMER_SHEET['ORDER_FIELDS']])
        # return tuple(Order.objects.filter(id=self.order.id).values_list(*settings.CUSTOMER_SHEET['ORDER_FIELDS'])[0])

    @property
    def product_quantities(self):
        return tuple([1,2,3,4,5])

    def to_df(self):
        df = pd.DataFrame([
            self.headers,
            self.pack_sizes,
            self.product_prices,
            self.order_details,
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
