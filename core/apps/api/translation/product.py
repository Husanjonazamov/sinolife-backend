from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ProductimageModel, ProductModel


@register(ProductModel)
class ProductTranslation(TranslationOptions):
    fields = [
        "title",
        "description",
    ]


@register(ProductimageModel)
class ProductimageTranslation(TranslationOptions):
    fields = []
