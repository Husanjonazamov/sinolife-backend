from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import ProductModel

from django.utils.safestring import mark_safe



@admin.register(ProductModel)
class ProductAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id_badge",
        "title_badge",
        "category_colored",
        "discounted_price_badge",
        "price_badge",
        "image_tag",
        "quantity_badge",
        "is_new_badge",
        "is_discounted_badge",
    )

    def id_badge(self, obj):
        return mark_safe(
            f'<span style="padding:4px 8px; color:#2980b9; font-weight:bold;">{obj.id}</span>'
        )
    id_badge.short_description = "ID"


    def category_colored(self, obj):
        if obj.category:
            return mark_safe(
                f'<span style="padding:4px 8px; color:#27ae60; font-weight:bold;">{obj.category.title}</span>'
            )
        return "-"
    category_colored.short_description = "Kategoriya"


    def title_badge(self, obj):
        return mark_safe(
            f'<span style="font-weight:bold; font-size: 15px;">{obj.title}</span>'
        )
    title_badge.short_description = "Nomi"



    def discounted_price_badge(self, obj):
        return mark_safe(
            f'<span style="color:white; padding:3px 7px; border-radius:5px;">{obj.discounted_price} so‘m</span>'
        )
    discounted_price_badge.short_description = "Chegirma narxi"

    def price_badge(self, obj):
        return mark_safe(
            f'<span style="color:white; padding:3px 7px; border-radius:5px;">{obj.price} so‘m</span>'
        )
    price_badge.short_description = "Narxi"
    
    

    def quantity_badge(self, obj):
        return mark_safe(
            f'<span style="color:white; padding:3px 7px; border-radius:5px;">{obj.quantity} dona</span>'
        )
    quantity_badge.short_description = "Soni"
    
    

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="60" style="border-radius:8px; object-fit:cover;" />'
            )
        return "-"
    image_tag.short_description = "Rasm"

    def is_new_badge(self, obj):
        if obj.is_new:
            return mark_safe(
                '<span style="padding:4px 8px; border:1px solid #27ae60; color:#27ae60; border-radius:5px;">Faol</span>'
            )
        else:
            return mark_safe(
                '<span style="padding:4px 8px; border:1px solid #e74c3c; color:#e74c3c; border-radius:5px;">Faol emas</span>'
            )
    is_new_badge.short_description = "Yangi"

    def is_discounted_badge(self, obj):
        if obj.is_discounted:
            return mark_safe(
                '<span style="padding:4px 8px; border:1px solid #27ae60; color:#27ae60; border-radius:5px;">Faol</span>'
            )
        else:
            return mark_safe(
                '<span style="padding:4px 8px; border:1px solid #e74c3c; color:#e74c3c; border-radius:5px;">Faol emas</span>'
            )
    is_discounted_badge.short_description = "Chegirma"

