from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import BrandModel


@register(BrandModel)
class BrandTranslation(TranslationOptions):
    fields = []
