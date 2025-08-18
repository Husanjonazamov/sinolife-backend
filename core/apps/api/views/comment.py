from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import CommentModel
from core.apps.api.serializers.comment import CreateCommentSerializer, ListCommentSerializer, RetrieveCommentSerializer


@extend_schema(tags=["comment"])
class CommentView(BaseViewSetMixin, ModelViewSet):
    queryset = CommentModel.objects.all()
    serializer_class = ListCommentSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCommentSerializer,
        "retrieve": RetrieveCommentSerializer,
        "create": CreateCommentSerializer,
    }
