from rest_framework import serializers

from core.apps.api.models import MessagesModel


class BaseMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesModel
        fields = [
            "id",
            "name",
        ]


class ListMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta): ...


class RetrieveMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta): ...


class CreateMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
