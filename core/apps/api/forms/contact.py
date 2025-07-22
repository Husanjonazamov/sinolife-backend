from django import forms

from core.apps.api.models import ContactModel


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactModel
        fields = "__all__"
