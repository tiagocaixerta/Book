from rest_framework import serializers

from product.models.product import Category, Product
from product.serializers.category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(

        queryset=Category.objects.all(),
        write_only=True,
        many=True

        queryset=Category.objects.all(), write_only=True, many=True

    )

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "active",

            "category",         # leitura
            "categories_id",    # escrita

            "category",
            "categories_id",

        ]

    def create(self, validated_data):
        category_data = validated_data.pop("categories_id")
        product = Product.objects.create(**validated_data)
        product.category.set(category_data)
        return product

    def update(self, instance, validated_data):
        category_data = validated_data.pop("categories_id", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if category_data is not None:
            instance.category.set(category_data)

        return instance

    def validate_categories_id(self, value):
        if not value:
            raise serializers.ValidationError("Você deve escolher ao menos uma categoria.")
        return value

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)

        return product

