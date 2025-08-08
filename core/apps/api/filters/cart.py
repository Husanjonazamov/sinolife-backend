from django_filters import rest_framework as filters

from core.apps.api.models import CartitemModel, CartModel


class CartFilter(filters.FilterSet):
    tg_id = filters.NumberFilter(field_name="user__tg_id", lookup_expr="icontains")

    class Meta:
        model = CartModel
        fields = [
            "tg_id",
        ]


# class CartitemFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = CartitemModel
#         fields = [
#             "name",
#         ]
