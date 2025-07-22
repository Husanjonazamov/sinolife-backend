from rest_framework import serializers
from core.apps.api.serializers.product.product import ListProductSerializer
from core.apps.api.models import OrderitemModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = OrderitemModel
        fields = [
            "id",
            "product",
            "quantity"
        ]


    def get_product(self, obj):
        request = self.context.get('request')
        return ListProductSerializer(obj.product, context={"request": request}).data

class ListOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class RetrieveOrderitemSerializer(BaseOrderitemSerializer):
    class Meta(BaseOrderitemSerializer.Meta): ...


class CreateOrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderitemModel
        fields = [
            "product",
            "quantity",
        ]
