from rest_framework import serializers

from core.apps.api.models import CartitemModel, ProductModel
from core.apps.api.serializers.product import ListProductSerializer


class BaseCartitemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    
    class Meta:
        model = CartitemModel
        fields = [
            "id",
            "product",
            "quantity",
            "total_price"
        ]

    def get_product(self, obj):
        return ListProductSerializer(obj.product, context=self.context).data

class ListCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class RetrieveCartitemSerializer(BaseCartitemSerializer):
    class Meta(BaseCartitemSerializer.Meta): ...


class CreateCartitemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=ProductModel.objects.all())
    quantity = serializers.IntegerField(default=1)
    
    class Meta:
        model = CartitemModel
        fields = [
            "product",
            "quantity"
        ]
