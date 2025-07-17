from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from core.apps.api.models import CartitemModel, CartModel



@admin.register(CartModel)
class CartAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "user_tag",
        "total_price",
    )

    def colored_id(self, obj):
        return format_html(
            '<span style="color:#1976D2; font-weight:bold; font-size:15px; text-shadow: 0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
            obj.id
        )
    colored_id.short_description = "ID"

    def user_tag(self, obj):
        return format_html(
            '<span style="color:#D84315; font-weight:bold; font-size:14px; text-shadow: 0 1px 1px rgba(0,0,0,0.05);">{}</span>',
            obj.user.first_name
        )
    user_tag.short_description = "Foydalanuvchi"



@admin.register(CartitemModel)
class CartitemAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "cart_tag",
        "product_tag",
        "product_image",
        "total_price",
    )

    def colored_id(self, obj):
        return format_html(
            '<span style="color:#8E24AA; font-weight:bold; font-size:15px; text-shadow: 0 1px 1px rgba(0,0,0,0.1);">#{}</span>',
            obj.id
        )
    colored_id.short_description = "ID"

    def cart_tag(self, obj):
        return format_html(
            '<span style="color:#009688; font-weight:600; font-size:14px; text-shadow: 0 1px 1px rgba(0,0,0,0.08);">Cart #{}</span>',
            obj.cart.id
        )
    cart_tag.short_description = "Savatcha"

    def product_tag(self, obj):
        return format_html(
            '<span style="color:#388E3C; font-weight:600; font-size:14px; text-shadow: 0 1px 1px rgba(0,0,0,0.08);">{}</span>',
            obj.product.title
        )
    product_tag.short_description = "Mahsulot"

    def product_image(self, obj):
        if obj.product.image and hasattr(obj.product.image, 'url'):
            return format_html(
                '<img src="{}" style="height:50px; width:50px; object-fit:cover; '
                'border-radius:8px; box-shadow:0 2px 6px rgba(0,0,0,0.1);" />',
                obj.product.image.url
            )
        return format_html('<span style="color:#999;">Rasm yo‘q</span>')
    product_image.short_description = "Rasm"
