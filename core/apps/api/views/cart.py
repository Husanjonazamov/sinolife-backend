from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import CartitemModel, CartModel
from core.apps.api.serializers.cart import (
    CreateCartitemSerializer,
    CreateCartSerializer,
    ListCartitemSerializer,
    ListCartSerializer,
    RetrieveCartitemSerializer,
    RetrieveCartSerializer,
)
from rest_framework.response import Response
from rest_framework import status

from rest_framework.decorators import action


@extend_schema(tags=["cart"])
class CartView(BaseViewSetMixin, ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = ListCartSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartSerializer,
        "retrieve": RetrieveCartSerializer,
        "create": CreateCartSerializer,
    }
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        return CartModel.objects.filter(user=self.request.user)


@extend_schema(tags=["cartItem"])
class CartitemView(BaseViewSetMixin, ModelViewSet):
    queryset = CartitemModel.objects.all()
    serializer_class = ListCartitemSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCartitemSerializer,
        "retrieve": RetrieveCartitemSerializer,
        "create": CreateCartitemSerializer,
    }
    
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        return CartitemModel.objects.filter(cart__user=self.request.user)
    
    @action(methods=["delete"], detail=True, url_path="remove")
    def remove_item(self, request, pk=None):
        cart_item = self.get_object()
        cart_item.delete()
        return Response({"detail": "Item removed from cart."}, status=status.HTTP_200_OK)