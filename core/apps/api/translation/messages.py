from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import MessagesModel


@register(MessagesModel)
class MessagesTranslation(TranslationOptions):
    fields = []
