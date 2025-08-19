from rest_framework import serializers

from core.apps.api.models import BrandModel


class BaseBrandSerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    class Meta:
        model = BrandModel
        fields = [
            "id",
            "title",
            "image",
            "product_count"
        ]
        def get_product_count(self, obj):
            return obj.products.count()
        


class ListBrandSerializer(BaseBrandSerializer):
    class Meta(BaseBrandSerializer.Meta): ...


class RetrieveBrandSerializer(BaseBrandSerializer):
    class Meta(BaseBrandSerializer.Meta): ...


class CreateBrandSerializer(BaseBrandSerializer):
    class Meta(BaseBrandSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
