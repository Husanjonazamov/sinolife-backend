from rest_framework import serializers

from core.apps.api.models import OrderModel
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.api.serializers.order.orderItem import CreateOrderitemSerializer
from core.apps.api.models.order import OrderitemModel
from core.apps.api.serializers.order.send_telegram import send_order

class BaseOrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "user",
            "first_name",
            "phone",
            "payment_type",
            "lat",
            "lon",
            "total"
        ]
        
    def get_user(self, obj):
        return UserSerializer(obj.user, read_only=True).data


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(serializers.ModelSerializer):
    order_item = CreateOrderitemSerializer(many=True, write_only=True)

    
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "first_name",
            "phone",
            "payment_type",
            "lat",
            "lon",
            "total",
            "order_item"
        ]
        
        read_only_fields = ['total']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_item')
        user = self.context['request'].user

        order = OrderModel.objects.create(user=user, **validated_data, total=0)

        total_order_price = 0

        for item_data in order_items_data:
            product = item_data['product']
            quantity = item_data.get('quantity', 1)
            item_total = product.price * quantity

            OrderitemModel.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                total_price=item_total
            )

            total_order_price += item_total

        order.total = total_order_price
        send_order(order)
        order.save()
        
        
        cart = user.users.first()
        
        if cart:
            cart.cart_items.all().delete()
            
            cart.total_price = 0
            cart.save()

        return order
