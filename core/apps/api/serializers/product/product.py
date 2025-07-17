from rest_framework import serializers

from core.apps.api.models import ProductModel


class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "description",
            "category",
            "discounted_price",
            "price",
            "image",
            "quantity",
            "is_new",
            "is_discounted",
        ]


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
