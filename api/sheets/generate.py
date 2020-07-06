import os
from django.conf import settings
from typing import List
from product.models import Product
from order.models import Order
from django.db.models import QuerySet
from sheets.input_cleansing import zero_product_count
from shared.files import empty_directory, create_dir
import pandas as pd
import PyPDF2
import xlsxwriter
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

SPACER = ('',)

def event_customer_sheets_xlsx(f_event_id) -> str:
    '''Concatenate order dataframes
       Return: The merged dataframe
    '''
    dfs = []

    # for each order, create the dataframe
    for ord in Order.objects.filter(fulfillment_event_id=f_event_id):
        g = CustomerSheet(ord)
        dfs.append(g.to_df())
    return pd.concat(dfs)


def event_customer_sheets(f_event_id) -> str:
    '''Generate customer sheets for an event
       Return: path to file
    '''

    create_dir(settings.CUSTOMER_SHEETS_PATH)
    empty_directory(settings.CUSTOMER_SHEETS_PATH)
    DEST_FILENAME = f'{f_event_id}_customer_sheets.pdf'
    DEST_PATH = os.path.join(settings.CUSTOMER_SHEETS_PATH, DEST_FILENAME)

    pdfWriter = PyPDF2.PdfFileWriter()
    # Generate all events PDFs individually
    for ord in Order.objects.filter(fulfillment_event_id=f_event_id):
        g = CustomerSheet(ord)
        g.to_pdf()

    # Then merge/concatenate
    for filename in sorted(os.listdir(settings.CUSTOMER_SHEETS_PATH)):
        if (filename != DEST_FILENAME):
            pdfFileObj = open(os.path.join(settings.CUSTOMER_SHEETS_PATH,filename),'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for pageNum in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
                pdfOutput = open(DEST_PATH, 'wb')
                pdfWriter.write(pdfOutput)
                pdfOutput.close()

    return DEST_PATH

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
        qs_pq = self.order.product_quantities.all()
        product_names = [p_q.product.name for p_q in qs_pq]
        # product_names = list(self.order.products.values_list('name',flat=True))
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

        converted_product_prices = tuple([str(f'£{c}') for c in product_prices])
        return product_prices_empty_cells + ('Current Price',) + converted_product_prices + SPACER

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
        '''For each product header, what are the quantities'''
        return tuple(self.order.product_quantities.all().values_list('quantity',flat=True))

    @property
    def quantity_costs(self):
        HEADER = 'Cost'

        costs_empty_cells = (SPACER * len(self.customer_headers))
        # product_prices = tuple(self.order.products.values_list('price',flat=True))
        product_costs = self.order.products.values_list('price',flat=True)
        quantity_costs = []
        product_prices = tuple(self.order.products.values_list('price',flat=True))
        for p,q in zip(product_prices, self.product_quantities):
            quantity_costs.append(p*q)

        gross_total = (f'£{sum(list(quantity_costs))}',)

        converted_product_costs = [str(f'£{c}') for c in quantity_costs]
        product_costs = tuple(converted_product_costs)
        return costs_empty_cells + (HEADER,) + product_costs + gross_total

    def to_df(self):
        SPACER_COLUMN = ('','','','','','','','', '','','','','','')
        df = pd.DataFrame([
            self.headers,
            self.pack_sizes,
            self.product_prices,
            self.order_details,
            self.quantity_costs,
        ])
        self._df_transposed = df.transpose()
        return self._df_transposed

    def to_pdf(self) -> str:
        '''
            Generate PDF, save to CUSTOMER_SHEETS_PATH
            return path Path to file
        '''
        create_dir(settings.CUSTOMER_SHEETS_PATH)
        self.to_df()
        dest_filename = f"{self.order.f_number}_customer_sheet.pdf"
        dest_path = os.path.join(settings.CUSTOMER_SHEETS_PATH,dest_filename)
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("customer_sheet.html")
        template_vars = {"title" : "Farmbox Customer Sheet",
                        "customer_sheet": self._df_transposed.to_html()}
        html_out = template.render(template_vars)
        HTML(string=html_out).write_pdf(dest_path, stylesheets=["style.css", "customer_sheet.css"])
        return dest_path



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
