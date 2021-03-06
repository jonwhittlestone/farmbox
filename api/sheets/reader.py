import os
import json
import re
import sys
from pathlib import Path
from decimal import Decimal
from datetime import datetime
from django.utils import timezone
from openpyxl import load_workbook
from product.models import Product
from customer.models import get_or_create_customer
from order.models import OrderForm, FulfillmentEvent, Order, ProductQuantity
from django.conf import settings
from django.forms import ValidationError
from django.db.utils import IntegrityError
from order.exceptions import OrderFormReaderException
from sheets.input_cleansing import OrderSheet as OrderSheetCleanser
from customer.models import Customer

FILENAME = os.path.basename(settings.SAMPLE_ORDER_SHEET_PATH)


def collect_files_for_reading(path=None) -> list:
    if not path:
        path = settings.SAMPLE_ORDER_SHEET_DIR
    xlsx_files = Path(path).glob("*.xlsx")
    return list(xlsx_files)


class SheetReader:
    filename: str
    excel_data: []
    _order: Order
    _customer: Customer
    obj: OrderForm
    cell_cleanser: OrderSheetCleanser
    _order_details: {}
    _product_counts: {}

    def __init__(self):
        self.cell_cleanser = OrderSheetCleanser()

    def create_order(
        self,
        f_event: FulfillmentEvent,
        customer: Customer,
        order_details=None,
        product_counts=None,
    ):
        """Creates the order and then adds the products"""
        if not order_details:
            order_details = self._order_details
        if not product_counts:
            product_counts = self._product_counts

        del order_details["fulfillment_event__target_date"]
        order_details["fulfillment_event_id"] = f_event.id
        order_details["created_at"] = timezone.now()
        order_details["modified_at"] = timezone.now()
        order_details["customer_id"] = customer.id
        self._order = Order(**order_details)
        # validate for uniqueness
        customer_email_exists_for_event = Order.objects.filter(
            fulfillment_event_id=f_event.id,
            customer_email=order_details["customer_email"],
        ).exists()
        if not order_details.get("customer_first_name", False):
            raise ValidationError("The customer_first_name cell should not be empty.")

        if customer_email_exists_for_event:
            raise ValidationError(
                f'Order with email: {order_details["customer_email"]} already exists for event {f_event}.'
            )
        self._order.save()
        for p_name, count in product_counts.items():
            if count is not None:
                p = Product.objects.filter(name=p_name).first()
                ProductQuantity.objects.create(
                    order=self._order, product=p, quantity=count
                )
        return self._order

    def read_to_model(self, file=None) -> Order:
        """Creates an Order model instance from an Order Sheet."""
        self.read(file)

        try:
            order_details = self.order_details
            self.product_counts
            f_event = self.get_or_create_fulfillment_event()
            self._customer = get_or_create_customer(order_details)
            self.create_order(f_event, self._customer)
        except (IntegrityError, ValidationError) as e:
            raise OrderFormReaderException(f"Problem saving the Order Model: {e}")
        else:
            self.obj.fulfillment_event = f_event
            self.obj.order = self._order
            self.obj.save()
            return self._order

    @property
    def customer(self):
        return self._customer

    def get_or_create_fulfillment_event(self, order_details=None):
        """
        Given parsed target_date, use existing f_event, or if date
        does not exist, create new model instance with that target_date
        """
        if not order_details:
            order_details = self._order_details

        if not order_details.get("fulfillment_event__target_date"):
            raise ValidationError(
                "The form is missing a fulfillment event target date."
            )

        try:
            converted_date = order_details.get("fulfillment_event__target_date")
            if not isinstance(converted_date, datetime):
                format_string = "%d/%m/%Y"
                converted_date = datetime.strptime(converted_date, format_string)
        except Exception as e:
            raise ValidationError(f"Date Issues: {e}")

        f_event_obj, created = FulfillmentEvent.objects.get_or_create(
            target_date=converted_date
        )
        f_event_obj.target_date = converted_date
        f_event_obj.save()

        self.obj.fulfillment_event = f_event_obj
        return f_event_obj

    def read(self, xlsx_file=None):
        if not xlsx_file:
            xlsx_file = os.path.join(settings.SAMPLE_ORDER_SHEET_DIR, FILENAME)
        self.obj = OrderForm.objects.create(
            filename=xlsx_file, created_at=timezone.now()
        )
        workbook = load_workbook(filename=xlsx_file, read_only=True)
        worksheet = workbook.active
        self.excel_data = list(worksheet.rows)
        return self.excel_data

    def cell_cleaner(self, value, field=""):
        # Commenting out because value should be 'Collect from Ockley Shop'
        # not, 'Collection From Ockley Shop'
        if field == "collection_location" or field == "customer_last_name":
            return value.title()
        return value

    @property
    def order_details(self):
        self._order_details = {}
        cell_map = settings.ORDER_SHEET.get("DETAILS_CELL_MAP", {})
        for row in self.excel_data:
            for cell in row:
                try:
                    field = cell_map.get(cell.coordinate, "")
                    cleaned_value = self.cell_cleaner(cell.internal_value, field)
                    self._order_details[field] = cleaned_value
                except Exception as e:
                    print(f"[155] {e}")
        del self._order_details[""]
        return self._order_details

    @property
    def product_counts(self):
        self._product_counts = {}

        # product names
        products = list(
            Product.objects.filter(published=True).values_list("name", flat=True)
        )
        products_rows = []

        # first pass to capture all cell.row where there are valid products
        for row in self.excel_data:
            for cell in row:
                if cell.value is None:
                    break
                if (
                    cell.column_letter
                    == settings.ORDER_SHEET.get("PRODUCT_NAME_COL", "")
                    and cell.internal_value in products
                ):
                    products_rows.append(row)

        if len(products_rows) == 0:
            raise ValidationError(
                '[182] The products on the customer sheet did not match product listing. Does this spreadsheet conform to the layout in "current.xlsx"?'
            )

        for row in products_rows:
            print(row)
            for cell in row:
                if not hasattr(cell, "column_letter"):
                    break
                if cell.column_letter == settings.ORDER_SHEET.get("PRODUCT_NAME_COL"):
                    key = cell.internal_value
                if cell.column_letter == settings.ORDER_SHEET.get("PRODUCT_COUNT_COL"):
                    value = self.cell_cleanser.product_count(cell.internal_value)
                    # value = cell.internal_value
            try:
                self._product_counts[key] = value
            except Exception:
                break
        return self._product_counts


class OrderSheet(SheetReader):
    def __init__(self):
        self.cell_cleanser = OrderSheetCleanser()


class ProductSelectionSheet(SheetReader):

    _product_details: []

    def __init__(self):
        super(SheetReader, self).__init__()

    @property
    def product_details(self):
        self._product_details = []
        prod_regex = r"[A-z][0-9]+$"

        for row in self.excel_data:
            is_match = False
            for cell in row:
                if cell.value is None:
                    break
                if cell.column_letter == settings.ORDER_SHEET.get(
                    "PRODUCT_NAME_COL", ""
                ):
                    is_match = []
                    is_match = re.findall(prod_regex, cell.internal_value)
                    if len(is_match) > 0:
                        try:
                            self._product_details.append(
                                {
                                    "name": row[0].value,
                                    "code": re.findall("[A-Z]{2}[0-9]*$", row[0].value)[
                                        0
                                    ],
                                    "price": Decimal(row[3].value),
                                }
                            )
                        except Exception:
                            continue
        return self._product_details

    def get_products(self, file):
        self.read(file)
        return self.product_details
