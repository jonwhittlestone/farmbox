from django.test import TestCase
from order.models import Order
from shared.tests import user_allowed, create_user, login_user
import factory
import pytest
from pytest_factoryboy import register

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

register(OrderFactory)

def test_pytest_can_be_run_from_vscode_by_ensuring_the_workspace_is_api_and_hit_f5():
    assert True == True


@pytest.mark.django_db
def test_factory_boy_integrated():
    ord = OrderFactory(customer_name='Jon Whittlestone')
    assert ord.customer_name == 'Jon Whittlestone'


@pytest.mark.django_db
def test_download_input_xlsx_responds_with_200(client):
    user,client = user_allowed(client)
    res = client.get('/api/order/input-sheet/1/')
    assert res.status_code == 200

# def test_