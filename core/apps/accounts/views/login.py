from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from core.services import UserService, SmsService

from rest_framework import status



User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer, UserService):
    def validate(self, attrs):
        data = super().validate(attrs)

        phone = self.user.phone  

        self.send_confirmation(phone)
        data['message'] = _("Sms %(phone)s raqamiga yuborildi") % {"phone": phone}
        
        return data         

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer