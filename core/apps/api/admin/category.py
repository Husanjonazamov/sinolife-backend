from django.utils.safestring import mark_safe
from django.contrib import admin
from unfold.admin import ModelAdmin
from core.apps.api.models import CategoryModel
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id_badge",
        "title_display",
    )

    def id_badge(self, obj):
            return mark_safe(
            f'<span style="padding:4px 8px; color:#2980b9; font-weight:bold;">{obj.id}</span>'
        )
    id_badge.short_description = "ID"

    def title_display(self, obj):
        return mark_safe(
            f'<span style="font-size:14px; font-weight:500;">{obj.title}</span>'
        )
    title_display.short_description = "Kategoriya nomi"
