from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BannerModel
from django.utils.safestring import mark_safe


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin):
    list_display = (
        "colored_id",
        "image_tag",
    )
    
    def colored_id(self, obj):
        return mark_safe(f'<span style="color: #0ef;">{obj.id}</span>')
    colored_id.short_description = "ID"

    def image_tag(self, obj):
        if obj.image:  
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" style="border-radius: 10px; object-fit: cover;" />'
            )
        return "-"
    image_tag.short_description = "Rasm"