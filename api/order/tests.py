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
    class Meta:
        model = Order

class FulfillmentEventFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FulfillmentEvent

register(OrderFactory)
register(ProductFactory)
register(FulfillmentEventFactory)

def test_pytest_can_be_run_from_vscode_by_ensuring_the_workspace_is_api_and_hit_f5():
    assert True == True


@pytest.mark.django_db
def test_factory_boy_integrated():
    ord = OrderFactory(customer_name='Jon Whittlestone')
    assert ord.customer_name == 'Jon Whittlestone'


@pytest.mark.django_db
def test_download_input_xlsx_returns_byte_stream(client):
    assert False
    user,client = user_allowed(client)
    res = client.get('/api/order/input-sheet/1/')
    assert res.status_code == 200

from django.utils import timezone
inline_sample_orders = [
    {
        'customer_name': '[NotARealOrder] Christopher Koliba',
        'customer_address': '11 Lonsdale Place, Dorking',
        'customer_postcode': 'RH4 2WJ',
        'customer_email': 'dev+farmbox@howapped.com',
        'customer_phone': '0789 449 5422',
        'fulfillment_method': 'Delivery',
        'collection_location': 'Denbies',
        'notes': '04-Mar',
        'created_at': timezone.now(),
        'modified_at': timezone.now(),
    },
]

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
        orders, products = [],[]
        f_event = FulfillmentEvent.objects.first()
        # products
        # create sample fulfillment event
        # f_event = FulfillmentEventFactory(**sample_fulfillment_events[0])

        # create sample products
        # for initial_p in initial_products:
        #     p = ProductFactory(**initial_p)
        #     p.save()
        #     products.append(p)

        # add orders
        # for i,sample in enumerate(sample_orders):
            # sample['fulfillment_event_id'] = f_event.id
            # print(sample)
            # order = OrderFactory(**sample)
            # order.fulfillment_event = f_event
            # order.id = i+1
            # order.save()
            # orders.append(order) 

        # add X number of products to order
        # for ord in orders:
        #     NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER = 5           
        #     valid_products_ids = Product.objects.all().values_list('id', flat=True)
        #     ids = list(valid_products_ids)
        #     random_products_ids = random.sample(ids, min(len(ids), NUMBER_PRODUCTS_TO_ADD_TO_A_SAMPLE_ORDER))
        #     qs = Product.objects.filter(id__in=random_products_ids)
        #     for p in qs:
        #         ord.products.add(p)
        # f_event_id_db = Order.objects.all()[0].fulfillment_event_id
        # debug=True
        # return {
        #     'f_event': f_event,
        #     'orders': orders,
        #     'all_products': products
        # }


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

    def test_a_list_of_lists_is_created_for_headers_and_customer_details(self):
        '''
            Create the untransposed multi-dimensional list containing
            order product counts
        '''
        maker = InputSheet()
        # construct header columns and test
        # The header list will be one or more columns of the generated xlsx
        customer_headers = maker.customer_headers
        product_headers = maker.product_headers
        # assert headers == [maker.customer_headers + maker.product_headers]
        headers = [maker.customer_headers + maker.product_headers]
        assert headers == maker.headers

        testing_f_event_id = Order.objects.all()[0].fulfillment_event_id
        # get customer order columns
        cols = maker.order_cols(testing_f_event_id)

        # assert one of the contents of product counts, matches 
        # the order's product count held in the database
        # find_a_product_row_containing_a_non_zero
        for i in range(0,len(product_headers)):
            pass
        
        # assert cols count matches the count of orders for the event

        debug = True

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
        assert False

        self.clean_up()
