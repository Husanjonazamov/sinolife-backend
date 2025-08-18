from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import CommentModel


@register(CommentModel)
class CommentTranslation(TranslationOptions):
    fields = []
