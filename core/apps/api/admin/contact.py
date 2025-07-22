from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ContactModel

@admin.register(ContactModel)
class ContactAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "colored_id",
        "phone_tag",
        "address_tag",
        "telegram_tag",
    )

    def colored_id(self, obj):
            return format_html(
            '<span style="color:#1976D2; font-weight:bold; font-size:14px; text-shadow:0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
            obj.id
        )
    colored_id.short_description = "ID"


    def phone_tag(self, obj):
        return format_html(
            '<span style="color:#2E7D32; font-weight:500; font-size:13px;">{}</span>',
            obj.phone
        )
    phone_tag.short_description = "Telefon"

    def address_tag(self, obj):
        text = Truncator(obj.address).chars(50)  # 50 ta belgidan oshsa "..."
        return format_html(
            '<span style="color:#6A1B9A; font-weight:500; font-size:13px;">{}</span>',
            text
        )
    address_tag.short_description = "Manzil"

    def telegram_tag(self, obj):
        username = obj.telegram.replace("https://t.me/", "").replace("http://t.me/", "").strip()
        return format_html(
            '<a href="https://t.me/{0}" target="_blank" style="color:#1976D2; font-weight:500; font-size:13px;">t.me/{0}</a>',
            username
        )
    telegram_tag.short_description = "Telegram"
