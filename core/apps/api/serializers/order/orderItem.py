from rest_framework import serializers

from core.apps.api.models import OrderitemModel


class BaseOrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderitemModel
        fields = [
            "id",
            "product",
            "quantity"
        ]


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
