from rest_framework import serializers

from core.apps.api.models import CategoryModel


class BaseCategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()

    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "title",
            "image",
            "product_count"
        ]
    def get_product_count(self, obj):
        return obj.products.count()


class ListCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class RetrieveCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta): ...


class CreateCategorySerializer(BaseCategorySerializer):
    class Meta(BaseCategorySerializer.Meta):
        fields = [
            "id",
            "title",
        ]
