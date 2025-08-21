from rest_framework import serializers

from core.apps.api.models import OrderModel
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.api.serializers.order.orderItem import CreateOrderitemSerializer, BaseOrderitemSerializer
from core.apps.api.models.order import OrderitemModel
from core.apps.api.serializers.order.send_telegram import send_order
from core.apps.api.enums.payment_type import order_payment_type
from core.apps.accounts.models.user import User




class BaseOrderSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    order_items = serializers.SerializerMethodField()
    
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
            "status",
            "payment_status",
            "created_at",
            "order_items",
            "total"
        ]
        
    def get_order_items(self, obj):
        request = self.context.get("request")
        return BaseOrderitemSerializer(obj.order_items.all(), many=True, context={"request": request}).data  # ✅

    
    def get_user(self, obj):
        return UserSerializer(obj.user, read_only=True).data


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...

class CreateOrderSerializer(serializers.ModelSerializer):
    order_item = CreateOrderitemSerializer(many=True, write_only=True)
    tg_id = serializers.IntegerField(write_only=True, required=False)

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
            "status",
            "payment_status",
            "created_at",
            "region",   # ✅ qo‘shildi
            "district", # ✅ qo‘shildi
            "address",  # ✅ qo‘shildi
            "pay_link",
            "order_item",
            "tg_id",
        ]
        read_only_fields = ['total', 'status', 'payment_status', 'created_at', 'pay_link']

    def create(self, validated_data):
        request = self.context.get('request')
        order_items_data = validated_data.pop('order_item')
        tg_id = validated_data.pop('tg_id', None)

        # 1️⃣ Web sayt (token orqali)
        if request and request.user.is_authenticated:
            user = request.user
        # 2️⃣ Telegram bot (tg_id orqali)
        elif tg_id:
            user = User.objects.filter(tg_id=tg_id).first()
            if not user:
                raise serializers.ValidationError({'tg_id': "Foydalanuvchi topilmadi."})
        else:
            raise serializers.ValidationError("Foydalanuvchi aniqlanmadi (token yoki tg_id yo‘q).")

        # Buyurtma yaratish
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

        # Umumiy narx va to‘lov linkini yangilash
        order.total = total_order_price
        order.pay_link = order_payment_type(order)
        order.save()
        send_order(order)
        
        

        # Savatni tozalash
        cart = getattr(user, 'users', None)
        if cart:
            cart = cart.first()
            if cart:
                cart.cart_items.all().delete()
                cart.total_price = 0
                cart.save()

        return order
