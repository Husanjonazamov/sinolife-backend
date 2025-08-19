from django_filters import rest_framework as filters

from core.apps.api.models import ProductimageModel, ProductModel


class ProductFilter(filters.FilterSet):
    category_ids = filters.BaseInFilter(field_name="category_id", lookup_expr="in")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    is_populer = filters.BooleanFilter(field_name="is_populer")
    is_new = filters.BooleanFilter(field_name="is_new")
    is_discounted = filters.BooleanFilter(field_name="is_discounted")
    category = filters.CharFilter(field_name="category__title", lookup_expr="iexact")
    brand = filters.CharFilter(field_name="brand__title", lookup_expr="iexact")
    title = filters.CharFilter(field_name="title", lookup_expr="iexact")

    class Meta:
        model = ProductModel
        fields = [
            "category_ids",
            "category",
            "brand",
            "title",
            "min_price",
            "max_price",
            "is_populer",
            "is_new",
            "is_discounted",
        ]


# class ProductimageFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = ProductimageModel
#         fields = [
#             "name",
#         ]
