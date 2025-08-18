from rest_framework import serializers

from core.apps.api.models import ProductModel
from core.apps.api.serializers.category import BaseCategorySerializer
from core.apps.api.serializers.product.currency import BaseCurrencyPriceMixin
from core.apps.api.serializers.comment.comment import ListCommentSerializer


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
    images = serializers.SerializerMethodField()
    comments = ListCommentSerializer(many=True, read_only=True)  

    class Meta(BaseProductSerializer.Meta):
        fields = list(BaseProductSerializer.Meta.fields) + ["images", "comments"]

    def get_images(self, obj):
        request = self.context.get("request")
        images = obj.products.all()
        return [
            request.build_absolute_uri(image.image.url)
            if image.image else None
            for image in images
        ]


class CreateProductSerializer(BaseProductSerializer):
    class Meta(BaseProductSerializer.Meta):
        fields = [
            "id",
            "title",
        ]
