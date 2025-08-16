from rest_framework import serializers

from core.apps.api.models import ProductimageModel


class BaseProductimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductimageModel
        fields = [
            "id",
            "name",
        ]


class ListProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta): ...


class RetrieveProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta): ...


class CreateProductimageSerializer(BaseProductimageSerializer):
    class Meta(BaseProductimageSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
