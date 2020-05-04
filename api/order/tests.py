import random
import factory
import pytest
from djmoney.money import Money
from django.test import TestCase
from django.conf import settings
from product.models import Product
from order.models import Order, FulfillmentEvent
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
        'customer_name':'Jon Whittlestone',
        'fulfillment_event_id': f_event.id,
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    }

    count_of_orders_in_db_before_factory = Order.objects.all().count()
    ord = OrderFactory(**sample)
    order_qs = Order.objects.all().last()

    assert Order.objects.all().count() == count_of_orders_in_db_before_factory + 1
    assert order_qs.id != None
    assert order_qs.customer_name == 'Jon Whittlestone'
    assert order_qs.fulfillment_event_id == f_event.id


@pytest.mark.django_db
def test_download_input_xlsx_returns_byte_stream(client):
    pass
    # assert False
    user,client = user_allowed(client)
    res = client.get('/api/order/input-sheet/1/')
    assert res.status_code == 200

from django.utils import timezone
from sheets.generate import InputSheet

@pytest.mark.django_db
class TestGeneratingInputSheet:
    '''Tests for creating the input sheet from Order records.'''

    def clean_up(self):
        Order.objects.all().delete()
        Product.objects.all().delete()
        FulfillmentEvent.objects.all().delete()

    @pytest.fixture
    def event_orders_products(self):
        # self.clean_up()
        orders, products = [],[]
        # f_event = FulfillmentEvent.objects.first()
        # create sample fulfillment event
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

        debug=True
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

        debug = True
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
        ProductFactory(name='Meat', sequence=1, price=Money(1.50))
        ProductFactory(name='Veg', sequence=2, price=Money(1))
        maker = InputSheet()
        assert expected == maker.product_headers

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
