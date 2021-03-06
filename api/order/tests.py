import random
import factory
import pytest
from decimal import Decimal
from djmoney.money import Money
from collections import OrderedDict
from pandas.core.frame import DataFrame
from django.test import TestCase
from django.conf import settings
from product.models import Product
from order.models import Order, FulfillmentEvent, ProductQuantity
from shared.tests import user_allowed, create_user, login_user
from pytest_factoryboy import register
from order.fixtures import sample_fulfillment_events, sample_orders
from product.fixtures import initial_products


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

class OrderFactory(factory.django.DjangoModelFactory):
    # fulfillment_event_id = 3
    # user_id = 1

    class Meta:
        model = Order

        # django_get_or_create = ('customer_name',)

class FulfillmentEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FulfillmentEvent

register(OrderFactory)
register(ProductFactory)
register(FulfillmentEventFactory)


@pytest.mark.django_db
def test_factory_boy_integrated():

    f_event = FulfillmentEventFactory(**sample_fulfillment_events[0])
    sample = {
        'customer_first_name':'Jon',
        'customer_last_name':'Whittlestone',
        'fulfillment_event_id': f_event.id,
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    }

    count_of_orders_in_db_before_factory = Order.objects.all().count()
    ord = OrderFactory(**sample)
    full_name = f"{sample.get('customer_first_name')} {sample.get('customer_last_name')}"
    assert ord.customer_name == full_name


@pytest.mark.django_db
def test_download_input_xlsx_returns_byte_stream(client):
    pass
    # assert False
    user,client = user_allowed(client)
    res = client.get('/api/order/input-sheet/1/')
    assert res.status_code == 200


@pytest.mark.django_db
def test_i_can_get_the_total_price_for_an_orders_products():
    ord = Order.objects.first()
    actual = ord.products_price_total
    assert isinstance(actual, Decimal)
    assert actual != Decimal(0)

from django.utils import timezone
from sheets.generate import InputSheet, CustomerSheet


@pytest.mark.django_db
class TestGeneratingCustomerSheet:

    '''Tests for creating the input sheet from Order records.'''
    def test_the_column_of_dataframe_comprises_order_details_and_products(self):
        '''The first column of the sheet should comprise customer order details and the product names/codes'''
        DATAFRAME_COLUMN = 1
        order = Order.objects.all().first()
        t_obj = CustomerSheet(order)
        expected_product_names = tuple(order.products.values_list('name',flat=True))
        expected = ('F-Number', 'First Name', 'Last Name', 'Postcode',
                    'Address', 'Fulfillment Method', 'Event Date', '') + expected_product_names + ('TOTAL',)
        df = t_obj.to_df()
        assert isinstance(df, DataFrame)
        assert tuple(df[DATAFRAME_COLUMN - 1]) == expected

    def test_the_column_of_dataframe_comprises_packsizes(self):
        DATAFRAME_COLUMN = 2
        order = Order.objects.all().first()
        t_obj = CustomerSheet(order)
        df = t_obj.to_df()

        pack_sizes = tuple(order.products.values_list('pack_size',flat=True))
        assert tuple(df[DATAFRAME_COLUMN - 1])[8] == pack_sizes[0]
        assert tuple(df[DATAFRAME_COLUMN - 1])[9] == pack_sizes[1]
        assert tuple(df[DATAFRAME_COLUMN - 1])[10] == pack_sizes[2]

    def test_the_column_of_dataframe_comprises_prices(self):
        DATAFRAME_COLUMN = 3
        order = Order.objects.all().first()
        t_obj = CustomerSheet(order)
        df = t_obj.to_df()

        prices = tuple(order.products.values_list('price',flat=True))
        assert tuple(df[DATAFRAME_COLUMN - 1])[8] == f'£{str(prices[0])}'
        assert tuple(df[DATAFRAME_COLUMN - 1])[9] == f'£{prices[1]}'
        assert tuple(df[DATAFRAME_COLUMN - 1])[10] == f'£{prices[2]}'

    def test_the_column_of_dataframe_comprises_order_details_and_quantites(self):
        DATAFRAME_COLUMN = 4
        order = Order.objects.all().first()
        t_obj = CustomerSheet(order)
        df = t_obj.to_df()
        df_col = df[DATAFRAME_COLUMN - 1]

        # assert the first N indices contain the customer_details
        # as per the settings
        # coerce fulfillment event date into the expected fields
        expected_customer_details = list(Order.objects.filter(id=order.id).values_list(*settings.CUSTOMER_SHEET['ORDER_FIELDS'])[0])
        expected_customer_details[-1] = FulfillmentEvent.objects.get(id=expected_customer_details[-1])
        expected_customer_details = tuple(expected_customer_details)

        assert tuple(expected_customer_details) == tuple(df_col[0:len(settings.CUSTOMER_SHEET['ORDER_FIELDS'])])

        # assert position 7 contains the header 'Quantity'
        expected_header = 'Quantity'
        assert expected_header == df_col[len(settings.CUSTOMER_SHEET['ORDER_FIELDS'])]

        # assert the last cell values is equal to model instance
        # calculated total quantity
        last_cell = -1
        pq = OrderedDict({})
        for p in order.products.all():
            pq[p.name] = ProductQuantity.objects.get(order_id=order.id,product_id=p.id).quantity
        expected_quant_sum =sum(list(pq.values()))
        assert tuple(df_col)[last_cell] == expected_quant_sum

        # assert remaining cells contain product quantities
        # assert tuple(df[DATAFRAME_COLUMN - 1]) == expected
        start = len(expected_customer_details)+1
        stop = last_cell
        expected_quantities = tuple(pq.values())
        assert expected_quantities == tuple(df_col[start:stop])


    @pytest.mark.skip(reason="todo")
    def test_the_data_frame_column_contains_quanitity_costs(self):

        DATAFRAME_COLUMN = 5
        order = Order.objects.all().first()
        t_obj = CustomerSheet(order)
        df = t_obj.to_df()
        df_col = df[DATAFRAME_COLUMN - 1]
        # test last column is net total cost
        expected_total_cost = '£14.60'
        expected_costs =    ('','','','','','', '','Cost','£1.00','£2.60','£11.00','£3.00','£2.50',expected_total_cost)
        assert expected_costs == tuple(df_col)


@pytest.mark.django_db
class TestGeneratingInputSheet:

    def clean_up(self):
        Order.objects.all().delete()
        Product.objects.all().delete()
        FulfillmentEvent.objects.all().delete()

    @pytest.fixture
    def event_orders_products(self):
        orders, products = [],[]
        f_event = FulfillmentEventFactory(**sample_fulfillment_events[0])

        # no need to create sample products
        # as they will have already
        # been migrated

        # add orders
        for i,sample in enumerate(sample_orders):
            sample['fulfillment_event_id'] = f_event.id
            order = OrderFactory(**sample)
            order.id = i+1
            order.save()
            orders.append(order)

        # add X number of products to order
        for ord in orders:
            NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER = 5
            valid_products_ids = Product.objects.all().values_list('id', flat=True)
            ids = list(p.id for p in products)
            random_products_ids = random.sample(ids, min(len(ids), NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER))
            qs = Product.objects.filter(id__in=random_products_ids)

            for p in qs:
                from order.models import ProductQuantity
                ProductQuantity.objects.create(order=ord, product=p, quantity=random.randint(1,3))

        return {
            'f_event': f_event,
            'orders': orders,
            'all_products': products
        }


    def test_a_list_of_lists_is_created_for_headers_and_customer_details(self,event_orders_products):
        '''
            Create the untransposed multi-dimensional list containing
            order product counts
        '''
        maker = InputSheet()
        # construct header columns and test
        # The header list will be one or more columns of the generated xlsx
        customer_headers = maker.customer_headers
        product_headers = maker.product_headers
        headers = [maker.customer_headers + maker.product_headers]
        assert headers == maker.headers

        # get customer order columns
        cols = maker.order_cols(event_orders_products['f_event'].id)

        # assert cols count matches filter
        # the count of orders for the event
        product_start_idx = len(maker.customer_headers) - 1
        product_end_idx = len(headers) - 1
        email_idx = settings.INPUT_SHEET['ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS'].index(
            'customer_email')

        for output_ord_col in cols:
            for product_id,product_count in zip(maker.product_ids, range(product_start_idx, product_end_idx)):
                # print(f'ID {product_id}: {output_ord_col[product_count]}')
                db_ord = Order.objects.get(customer_email=output_ord_col[email_idx])
                assert output_ord_col[product_count] == db_ord.products.filter(id=product_id).count()

        self.clean_up()

    def test_for_input_sheet_headers_i_can_generate_a_list_of_customer_details(self, settings):
        expected = ['Email', 'If collection, which shop?']
        settings.INPUT_SHEET = {
            'ORDER_MODEL_CUSTOMER_DETAILS_HEADER_FIELDS':['customer_email', 'collection_location']
        }
        maker = InputSheet()
        assert expected == maker.customer_headers
        self.clean_up()

    def test_for_input_sheet_headers_i_can_generate_a_list_of_product_names(self, settings):
        expected = ['Meat', 'Veg']
        Product.objects.all().delete()
        ProductFactory(name='Meat', sequence=1, price=Money(1.50), published=True)
        ProductFactory(name='Veg', sequence=2, price=Money(1), published=True)
        maker = InputSheet()
        headers = maker.product_headers
        assert expected == headers

        # assert the count of product headers matches the count of products that aren't archived
        self.clean_up()



    def test_a_generated_xlsx_can_be_inspected_to_contain_expected_data(self):
        '''
            Generate xlsx via pandas dataframe
            Peer into it with openpyxl to see
            if it matches expected
            https://www.marsja.se/your-guide-to-reading-excel-xlsx-files-in-python/
        '''
        pass
        # clean up saved file

        # assert contents of product counts, matches
        # the order's product count held in the database
        # find_a_product_row_containing_a_non_zero

        # for i in range(0,len(product_headers)):
        #     pass


        self.clean_up()



@pytest.mark.django_db
class TestOrderFNumber:

    @pytest.fixture
    def order(self):

        f_event = FulfillmentEventFactory(**sample_fulfillment_events[0])
        sample = {
            'customer_first_name':'Jon ',
            'customer_last_name':'Mickelsson ',
            'customer_postcode': 'RH3 2KL',
            'customer_address': '14, High Street',
            'customer_email': 'jon+test@demon.co.uk',
            'customer_phone': '07889 4932222',
            'user_id':1,
            'fulfillment_event_id': f_event.id,
            'fulfillment_method': settings.FULFILLMENT_METHODS_DELIVERY,
            'created_at': timezone.now(),
            'modified_at': timezone.now(),
        }

        return Order.objects.create(**sample)


    @pytest.mark.django_db(transaction=True)
    def test_delivery_orders_have_correct_f_numbers_reassigned(self, order):
        '''
            Test f-number reassignment to delivery order f_numbers as new orders in
            different postcodes are added.

            > Series 1 to eg 60 :
            > These are deliveries arranged in post code order.
            > I 'cleanse' the list, ie retype RH55SS or RH 55SS etc to RH5 5SS and then simply sort.
            > Therefore when the drivers arrive at 9am / 9:30am / 10am they can
            > simply load the first available orders and they will be in
            > similar locations.
            > I don't divide the orders into rounds any more as the drivers can
            > take a different number of orders depending on the size of the
            > orders and the size of their cars.
            > They load the first 8 or whatever, and the next driver loads the next lot etc.
        '''
        keyed = {}
        # Test migrated orders have correct f_numbers
        for ord in Order.objects.all():
            keyed[ord.customer_email] = {
                'customer_email': ord.customer_email,
                'customer_postcode': ord.customer_postcode,
                'fulfillment_event_id': ord.fulfillment_event_id,
                'fulfillment_method': ord.fulfillment_method,
                'f_number': ord.f_number
            }

        assert keyed['dev+chriskoliba@howapped.com'].get('f_number') == f'2-0-002'
        assert keyed['dev+chriskoliba@howapped.com'].get('customer_postcode') == 'RH4 2WJ'

        assert keyed['dev+mavisharton@howapped.com'].get('f_number') == '2-0-003'
        assert keyed['dev+mavisharton@howapped.com'].get('customer_postcode') == 'RH5 4QX'

    @pytest.mark.skip()
    def test_f_number_generated_based_on_criteria(self):
        '''

            Series 100+ : these are the collect from Ockley.
            There is no arrangement within this group.
            If there are a lot then I divide them into two pick up times,
            ie 3-4pm and 4-5pm. eg 101 - 122 first hour,
            123 - 145 second hour.

            They all get picked up from Denbies at 2pm, in a large van, and
            taken down to Ockley.

            Series 200+ : these are the collect from Denbies.
            There is no arrangement within this group, but again if there
            are a lot I divide them into two groups for 3-4pm and 4-5pm pick up.
        '''
        pass
