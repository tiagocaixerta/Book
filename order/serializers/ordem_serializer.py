# order/serializers/order_serializer.py
from rest_framework import serializers
from product.serializers.product_serializers import ProductSerializer
from order.models.order import Order

class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        return sum(product.price for product in instance.products.all())

    class Meta:
        model = Order
        fields = ['products', 'total']
