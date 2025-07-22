from django import forms

from core.apps.api.models import MessagesModel


class MessagesForm(forms.ModelForm):

    class Meta:
        model = MessagesModel
        fields = "__all__"
