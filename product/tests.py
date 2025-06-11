import pytest
from product.models import Product
from product.factories import ProductFactory

@pytest.mark.django_db
def test_product_creation():
    product = ProductFactory()
    assert isinstance(product, Product)
    assert product.name is not None
    assert product.price is not None
