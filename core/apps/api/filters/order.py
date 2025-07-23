from django_filters import rest_framework as filters

from core.apps.api.models import OrderitemModel, OrderModel
from core.apps.api.enums.order import OrderPaymentStatusChoice, OrderStatusChoice


class OrderFilter(filters.FilterSet):
    status = filters.ChoiceFilter(
        field_name="status",
        choices=OrderStatusChoice.choices,
        label="Order Status"
    )
    payment_status = filters.ChoiceFilter(
        field_name="payment_status",
        choices=OrderPaymentStatusChoice.choices,
        label="Payment Status"
    )

    class Meta:
        model = OrderModel
        fields = ["status", "payment_status"]


# class OrderitemFilter(filters.FilterSet):
#     # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

#     class Meta:
#         model = OrderitemModel
#         fields = [
#             "name",
#         ]
