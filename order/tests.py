import pytest
from order.models import Order
from order.factories import OrderFactory
from product.factories import ProductFactory

@pytest.mark.django_db
def test_order_creation_with_user():
    order = OrderFactory()
    assert order.user is not None
    assert isinstance(order, Order)

@pytest.mark.django_db
def test_order_with_multiple_products():
    product1 = ProductFactory()
    product2 = ProductFactory()
    order = OrderFactory(product=[product1, product2])
    
    assert order.product.count() == 2
    assert product1 in order.product.all()
    assert product2 in order.product.all()
