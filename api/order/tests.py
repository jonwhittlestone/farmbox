from django.test import TestCase
from order.models import Order
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

