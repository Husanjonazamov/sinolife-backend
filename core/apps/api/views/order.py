from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import OrderitemModel, OrderModel
from core.apps.api.serializers.order import (
    CreateOrderitemSerializer,
    CreateOrderSerializer,
    ListOrderitemSerializer,
    ListOrderSerializer,
    RetrieveOrderitemSerializer,
    RetrieveOrderSerializer,
)

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from core.apps.api.filters.order import OrderFilter
from django_filters.rest_framework import DjangoFilterBackend





@extend_schema(tags=["order"])
class OrderView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = ListOrderSerializer
    filter_backends = [DjangoFilterBackend]  

    permission_classes = [IsAuthenticated]
    filterset_class = OrderFilter

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderSerializer,
        "retrieve": RetrieveOrderSerializer,
        "create": CreateOrderSerializer,
        "me": ListOrderSerializer
    }

    @action(detail=False, methods=['get'], url_path="me", permission_classes=[IsAuthenticated])
    def me(self, request):
        queryset = self.queryset.filter(user=request.user)

        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



@extend_schema(tags=["orderItem"])
class OrderitemView(BaseViewSetMixin, ModelViewSet):
    queryset = OrderitemModel.objects.all()
    serializer_class = ListOrderitemSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderitemSerializer,
        "retrieve": RetrieveOrderitemSerializer,
        "create": CreateOrderitemSerializer,
    }
