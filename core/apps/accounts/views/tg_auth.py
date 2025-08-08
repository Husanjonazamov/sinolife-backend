from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from core.apps.accounts.serializers.auth import TgRegisterSerializers, UserUpdateBotSerializer


from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin

User = get_user_model()






class TgRegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        phone = request.data.get("phone")
        
        if not phone:
            return Response({"phone": ["Telefon raqami majburiy."]}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone=phone)
            serializer = TgRegisterSerializers(user, data=request.data, partial=True)
        except User.DoesNotExist:
            serializer = TgRegisterSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class UserViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserUpdateBotSerializer
    permission_classes = [AllowAny]
    lookup_field = 'tg_id'  

    @action(detail=True, methods=['patch'], url_path='update-info')
    def update_info(self, request, tg_id=None):
        user = self.get_object()

        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)