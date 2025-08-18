from rest_framework import serializers

from core.apps.api.models import CommentModel


class BaseCommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = CommentModel
        fields = [
            "id",
            "user",
            "product",
            "message",
        ]
    
    def get_user(self, obj):
        from core.apps.accounts.serializers.user import UserSerializer
        return UserSerializer(obj.user).data if obj.user else None



class ListCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class RetrieveCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta): ...


class CreateCommentSerializer(BaseCommentSerializer):
    class Meta(BaseCommentSerializer.Meta):
        fields = [
            "id",
            "user",
            "product",
            "message",
        ]
        read_only_fields = ["user"]   

    def create(self, validated_data):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            validated_data["user"] = request.user  
        return super().create(validated_data)
