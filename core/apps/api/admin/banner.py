from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from core.apps.api.models import BannerModel
from django.utils.safestring import mark_safe




@admin.register(BannerModel)
class BannerAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "colored_id",
        "title_tag",
        "type",
        "subtitle_tag",
        "image_tag",
    )
    
    
    def colored_id(self, obj):
        return mark_safe(f'<span style="color: #0ef;">{obj.id}</span>')
    colored_id.short_description = "ID"
    
    def title_tag(self, obj):
        return mark_safe(f'<span style="font-size:14px; font-weight:600; color:#0ef;">{obj.title}</span>')
    
    title_tag.short_description = "Sarlavha"

    def subtitle_tag(self, obj):
        return mark_safe(f'<span style="font-size:12px; color:#888;">{obj.subtitle}</span>')
   
    subtitle_tag.short_description = "Qisqa matn"
    

    def image_tag(self, obj):
        if obj.image:  
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" style="border-radius: 10px; object-fit: cover;" />'
            )
        return "-"
    image_tag.short_description = "Rasm"