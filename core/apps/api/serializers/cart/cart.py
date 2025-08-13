from rest_framework import serializers

from core.apps.api.models import CartModel, CartitemModel
from core.apps.accounts.serializers.user import UserSerializer

from core.apps.api.serializers.cart.cartItem import CreateCartitemSerializer, ListCartitemSerializer
from django.db.models import Sum
from core.apps.accounts.models.user import User



class BaseCartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cart_items = serializers.SerializerMethodField()
    cart_items_count = serializers.SerializerMethodField()   # <-- Qo'shish shart!

    
    class Meta:
        model = CartModel
        fields = [
            "id",
            "user",
            "total_price",
            "cart_items_count",
            "cart_items"
        ]
        
    def get_cart_items(self, obj):
        return ListCartitemSerializer(
            obj.cart_items.all(), 
            many=True, 
            context=self.context   # <-- MUHIM!
        ).data
        
    def get_cart_items_count(self, obj):
        return obj.cart_items.count()


class ListCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class RetrieveCartSerializer(BaseCartSerializer):
    class Meta(BaseCartSerializer.Meta): ...


class CreateCartSerializer(serializers.ModelSerializer):
    cart_items = CreateCartitemSerializer(many=True, write_only=True)
    tg_id = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = CartModel
        fields = [
            "id",
            "tg_id",
            "cart_items",
        ]
        

    def create(self, validated_data):
        cart_items_data = validated_data.pop("cart_items")
        tg_id = validated_data.pop("tg_id")

        try:
            user = User.objects.get(tg_id=tg_id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"tg_id": "Foydalanuvchi topilmadi."})

        cart, created = CartModel.objects.get_or_create(user=user, defaults={"total_price": 0})

        for item_data in cart_items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            product_price = product.price
            item_total = product_price * quantity

            cart_item_qs = CartitemModel.objects.filter(cart=cart, product=product)
            if cart_item_qs.exists():
                cart_item = cart_item_qs.first()
                cart_item.quantity += quantity
                cart_item.total_price = cart_item.quantity * product_price
                cart_item.save()
            else:
                CartitemModel.objects.create(
                    cart=cart,
                    product=product,
                    quantity=quantity,
                    total_price=item_total
                )

        total = CartitemModel.objects.filter(cart=cart).aggregate(
            total=Sum('total_price')
        )['total'] or 0

        cart.total_price = total
        cart.save()

        return cart
