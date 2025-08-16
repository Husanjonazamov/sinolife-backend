from django import forms

from core.apps.api.models import ProductimageModel, ProductModel


class ProductForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = "__all__"


class ProductimageForm(forms.ModelForm):

    class Meta:
        model = ProductimageModel
        fields = "__all__"
