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
from core.apps.api.filters.cart import CartFilter
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.accounts.models.user import User




@extend_schema(tags=["cart"])
class CartView(BaseViewSetMixin, ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = ListCartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CartFilter
    permission_classes = [AllowAny]

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
        tg_id = self.request.query_params.get('tg_id')

        if self.request.user.is_authenticated:
            return CartModel.objects.filter(user=self.request.user)

        elif tg_id:
            try:
                user = User.objects.get(tg_id=tg_id)  
                return CartModel.objects.filter(user=user)
            except User.DoesNotExist:
                return CartModel.objects.none()

        return CartModel.objects.none()



    @action(detail=False, methods=['delete'], url_path="clear")
    def clear(self, request):
        tg_id = request.data.get("tg_id")
        try:
            user = User.objects.get(tg_id=tg_id)
            cart = CartModel.objects.get(user=user)
            
            cart.cart_items.all().delete()
            
            cart.total_price = 0
            cart.save()
            
            return Response({"detail": "Savat tozalandi"}, status=200)
        
        except User.DoesNotExist:
            return Response({"detail": "Foydalanuvchi topilmadi"}, status=404)
        except CartModel.DoesNotExist:
            return Response({"detail": "Savat topilmadi"}, status=404)      
        
        



@extend_schema(tags=["cartItem"])
class CartitemView(BaseViewSetMixin, ModelViewSet):
    queryset = CartitemModel.objects.all()
    serializer_class = ListCartitemSerializer
    permission_classes = [AllowAny]

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