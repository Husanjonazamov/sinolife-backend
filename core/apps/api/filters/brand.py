from django_filters import rest_framework as filters

from core.apps.api.models import BrandModel


class BrandFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")

    class Meta:
        model = BrandModel
        fields = [
            "title",
        ]
