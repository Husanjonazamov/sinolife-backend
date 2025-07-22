from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import ContactModel


@register(ContactModel)
class ContactTranslation(TranslationOptions):
    fields = [
        "address"
    ]
