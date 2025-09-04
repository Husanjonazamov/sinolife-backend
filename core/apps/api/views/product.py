from django.db.models import Q
from django_core.mixins import BaseViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.filters.product import ProductFilter
from core.apps.api.models import ProductimageModel, ProductModel
from core.apps.api.serializers.product import (
    BaseProductSerializer,
    CreateProductimageSerializer,
    CreateProductSerializer,
    ListProductimageSerializer,
    ListProductSerializer,
    RetrieveProductimageSerializer,
    RetrieveProductSerializer,
)


class ProductSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get("search", "")
        if query:
            products = ProductModel.objects.filter(title__icontains=query)
        else:
            products = ProductModel.objects.all()

        serializer = BaseProductSerializer(products, many=True, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(tags=["product"])
class ProductView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    ordering_fields = ["created_at", "price"]
    ordering = ["-created_at"]
    pagination_class = None

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
            queryset = queryset.filter(Q(title__icontains=q) | Q(category__title__icontains=q))

        return queryset
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            "status": True,
            "links": {
                "previous": None,
                "next": None,
            },
            "total_items": queryset.count(),
            "total_pages": 1,  # pagination yo‘q, doim 1 sahifa
            "page_size": queryset.count(),
            "current_page": 1,
            "results": serializer.data,
        }

        return Response(response_data)



@extend_schema(tags=["productImage"])
class ProductimageView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ProductimageModel.objects.all()
    serializer_class = ListProductimageSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListProductimageSerializer,
        "retrieve": RetrieveProductimageSerializer,
        "create": CreateProductimageSerializer,
    }
