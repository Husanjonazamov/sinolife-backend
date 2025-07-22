from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator
from unfold.admin import ModelAdmin

from core.apps.api.models import MessagesModel

@admin.register(MessagesModel)
class MessagesAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "first_name_tag",
        "phone_tag",
        "message_tag"
    )
    def colored_id(self, obj):
                return format_html(
                '<span style="color:#1976D2; font-weight:bold; font-size:14px; text-shadow:0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
                obj.id
            )
    colored_id.short_description = "ID"
        
    def first_name_tag(self, obj):
        return format_html(
            '<span style="color:#1976D2; font-weight:500; font-size:13px;">{}</span>',
            obj.first_name
        )
    first_name_tag.short_description = "Ism"

    def phone_tag(self, obj):
        return format_html(
            '<span style="color:#2E7D32; font-weight:500; font-size:13px;">{}</span>',
            obj.phone
        )
    phone_tag.short_description = "Telefon"

    def message_tag(self, obj):
        text = Truncator(obj.message).chars(50)  # 50 ta belgidan oshsa "..."
        return format_html(
            '<span style="color:#6A1B9A; font-weight:400; font-size:13px;">{}</span>',
            text
        )
    message_tag.short_description = "Xabar"
