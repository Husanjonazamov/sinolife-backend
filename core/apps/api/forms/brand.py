from django import forms

from core.apps.api.models import BrandModel


class BrandForm(forms.ModelForm):

    class Meta:
        model = BrandModel
        fields = "__all__"
