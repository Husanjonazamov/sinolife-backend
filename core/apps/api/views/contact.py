from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import ContactModel
from core.apps.api.serializers.contact import CreateContactSerializer, ListContactSerializer, RetrieveContactSerializer


@extend_schema(tags=["contact"])
class ContactView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ListContactSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListContactSerializer,
        "retrieve": RetrieveContactSerializer,
        "create": CreateContactSerializer,
    }
