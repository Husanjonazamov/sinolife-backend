from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.category import BaseCategorySerializer
from core.apps.api.serializers.product.currency import BaseCurrencyPriceMixin


class BaseProductSerializer(serializers.ModelSerializer, BaseCurrencyPriceMixin):
    image = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    discounted_price = serializers.SerializerMethodField()
    category = BaseCategorySerializer()
    
    class Meta:
        model = ProductModel
        fields = [
            "id",
            "title",
            "description",
            "image_id",
            "video_id",
            "category",
            "discounted_price",
            "price",
            "image",
            "quantity",
            "is_populer",
            "is_new",
            "is_discounted",
        ]
        
    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None
        
    def get_price(self, obj):
        return self.get_currency_price(obj.price or 0)
    
    def get_discounted_price(self, obj):
        return self.get_currency_price(obj.discounted_price or 0)


class ListProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class RetrieveProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta): ...


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
