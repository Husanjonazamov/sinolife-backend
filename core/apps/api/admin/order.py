from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin

from core.apps.api.models import OrderitemModel, OrderModel, OrderPaymentChoice


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "first_name_tag",
        "phone_tag",
        "payment_type_tag",
        "total_tag",
    )

    def colored_id(self, obj):
        return format_html(
            '<span style="color:#1976D2; font-weight:bold; font-size:14px; text-shadow:0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
            obj.id
        )
    colored_id.short_description = "ID"


    def first_name_tag(self, obj):
        return format_html(
            '<span style="color:#4E342E; font-weight:500; font-size:13px;">{}</span>',
            obj.first_name
        )
    first_name_tag.short_description = "Ism"

    def phone_tag(self, obj):
        return format_html(
            '<span style="color:#2E7D32; font-weight:500; font-size:13px;">{}</span>',
            obj.phone
        )
    phone_tag.short_description = "Telefon"

    def payment_type_tag(self, obj):
        if obj.payment_type == OrderPaymentChoice.CLICK:
            color = "#1565C0"  # Ko‘k (Click)
        elif obj.payment_type == OrderPaymentChoice.PAYME:
            color = "#2E7D32"  # Yashil (Payme)
        else:
            color = "#999"     # Default (no value)

        return format_html(
            '<span style="color:{}; font-weight:bold; font-size:13px;">{}</span>',
            color, obj.get_payment_type_display()
        )
    payment_type_tag.short_description = "To'lov turi"

    def total_tag(self, obj):
        return format_html(
            '<span style="color:#6A1B9A; font-weight:bold; font-size:14px;">{} so‘m</span>',
            obj.total
        )
    total_tag.short_description = "Jami"


@admin.register(OrderitemModel)
class OrderitemAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "order_tag",
        "product_tag",
        "quantity",
        "total_price_tag"
    )

    def colored_id(self, obj):
        return format_html(
            '<span style="color:#8E24AA; font-weight:bold; font-size:14px; text-shadow:0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
            obj.id
        )
    colored_id.short_description = "ID"

    def order_tag(self, obj):
        return format_html(
            '<span style="color:#0288D1; font-weight:600; font-size:13px;">Order #{}</span>',
            obj.order.id
        )
    order_tag.short_description = "Buyurtma"

    def product_tag(self, obj):
        return format_html(
            '<span style="color:#00796B; font-weight:500; font-size:13px;">{}</span>',
            obj.product.title
        )
    product_tag.short_description = "Mahsulot"

    def total_price_tag(self, obj):
        return format_html(
            '<span style="color:#F57C00; font-weight:bold; font-size:13px;">{} so‘m</span>',
            obj.total_price
        )
    total_price_tag.short_description = "Jami narx"
