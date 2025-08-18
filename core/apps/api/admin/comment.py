from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import CommentModel


@admin.register(CommentModel)
class CommentAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
