import pytest
from decimal import Decimal
from product.models import Product


@pytest.mark.django_db
def test_it_persists_the_new_selection():
    parsed = [
        {
            "name": "New Apples FV1",
            "code": "FV1",
            "price": Decimal(1.00),
        },
        {
            "name": "Village Greens Veg Bag : Large FV3355",
            "code": "FV3355",
            "price": Decimal(15.00),
        },
    ]

    expected_selection = []

    actual_persisted_new_selection = Product.write_new_selection(parsed)
    for i, p in enumerate(parsed):

        expected_selection.append(parsed[i])
        expected_selection[i]["published"] = True
        expected_selection[i]["sequence"] = i + 1

        assert (
            actual_persisted_new_selection[i]["name"] == expected_selection[i]["name"]
        )
        assert (
            actual_persisted_new_selection[i]["code"] == expected_selection[i]["code"]
        )
        assert (
            actual_persisted_new_selection[i]["price"] == expected_selection[i]["price"]
        )
        assert (
            actual_persisted_new_selection[i]["published"]
            == expected_selection[i]["published"]
        )
        assert (
            actual_persisted_new_selection[i]["sequence"]
            == expected_selection[i]["sequence"]
        )
