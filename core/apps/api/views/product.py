from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ProductModel
from core.apps.api.serializers.product import CreateProductSerializer, ListProductSerializer, RetrieveProductSerializer

from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from core.apps.api.filters.product import ProductFilter





@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductSerializer,
        "retrieve": RetrieveProductSerializer,
        "create": CreateProductSerializer,
    }
    
    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get("q")
        
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) |
                Q(category__title__icontains=q) 
            )
        
        
        return queryset
    
    
