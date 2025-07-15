from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import BannerModel
from django.utils.safestring import mark_safe


@admin.register(BannerModel)
class BannerAdmin(ModelAdmin):
    list_display = (
        "id",
        "image_tag",
    )

    def image_tag(self, obj):
        if obj.image:  
            return mark_safe(
                f'<img src="{obj.image.url}" width="80" style="border-radius: 10px; object-fit: cover;" />'
            )
        return "-"
    image_tag.short_description = "Rasm"