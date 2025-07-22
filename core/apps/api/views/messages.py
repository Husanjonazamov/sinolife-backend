from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import  ModelViewSet

from core.apps.api.models import MessagesModel
from core.apps.api.serializers.messages import (
    CreateMessagesSerializer,
    ListMessagesSerializer,
    RetrieveMessagesSerializer,
)


@extend_schema(tags=["messages"])
class MessagesView(BaseViewSetMixin, ModelViewSet):
    queryset = MessagesModel.objects.all()
    serializer_class = ListMessagesSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListMessagesSerializer,
        "retrieve": RetrieveMessagesSerializer,
        "create": CreateMessagesSerializer,
    }
