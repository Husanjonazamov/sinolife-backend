from django_filters import rest_framework as filters

from core.apps.api.models import ProductModel


class ProductFilter(filters.FilterSet):
    category_ids = filters.BaseInFilter(field_name='category_id', lookup_expr='in')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')


    class Meta:
        model = ProductModel
        fields = [
            "category_ids",
            "min_price",
            "max_price"
        ]
