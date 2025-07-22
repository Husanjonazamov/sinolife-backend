from rest_framework import serializers

from core.apps.api.models import MessagesModel
from .send_telegram import send_message


class BaseMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesModel
        fields = [
            "id",
            "first_name",
            "phone",
            "message",
        ]


class ListMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta): ...


class RetrieveMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta): ...


class CreateMessagesSerializer(BaseMessagesSerializer):
    class Meta(BaseMessagesSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "phone",
            "message"
        ]
        
    def create(self, validate_data):
        message = MessagesModel.objects.create(**validate_data)
        send_message(message=message)
        return message
