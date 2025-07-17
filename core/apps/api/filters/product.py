from django_filters import rest_framework as filters

from core.apps.api.models import ProductModel


class ProductFilter(filters.FilterSet):
    category_ids = filters.BaseInFilter(field_name='category_id', lookup_expr='in')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    is_populer = filters.BooleanFilter(field_name='is_populer')
    is_new = filters.BooleanFilter(field_name='is_new')
    is_discounted = filters.BooleanFilter(field_name='is_discounted')


    class Meta:
        model = ProductModel
        fields = [
            "category_ids",
            "min_price",
            "max_price",
            "is_populer",
            "is_new",
            "is_discounted"
        ]
