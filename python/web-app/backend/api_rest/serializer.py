from rest_framework import serializers
from .models import Product, Order, OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = OrderItem
        fields = ['product', 'product_id', 'quantity', 'price_at_order', 'subtotal']
        read_only_fields = ['price_at_order', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'order_date', 'items', 'total']
        read_only_fields = ['order_date', 'total']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create()

        for item in items_data:
            product = item['product']
            quantity = item['quantity']
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price_at_order=product.price
            )

        return order
