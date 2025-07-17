from django.contrib.auth import admin
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm  # UserCreationForm,
from unfold.forms import UserChangeForm

from django.utils.safestring import mark_safe



class CustomUserAdmin(admin.UserAdmin, ModelAdmin):
    change_password_form = AdminPasswordChangeForm
    # add_form = UserCreationForm
    form = UserChangeForm
    list_display = (
        "styled_first_name",
        "styled_phone",
        "styled_role",
    )
    
    autocomplete_fields = ["groups", "user_permissions"]
    fieldsets = ((None, {"fields": ("phone",)}),) + (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    
    def styled_first_name(self, obj):
            return mark_safe(f"<span style='color: #4CAF50; font-weight: bold;'>{obj.first_name}</span>")

    styled_first_name.short_description = "Ism"

    def styled_phone(self, obj):
        return mark_safe(f"<span style='color: #2196F3;'>{obj.phone}</span>")

    styled_phone.short_description = "Telefon"


    def styled_role(self, obj):
        color = "#f44336" if obj.role == "admin" else "#0BD205"
        return mark_safe(f"""
            <span style="
                border: 1px solid {color};
                color: {color};
                padding: 3px 8px;
                border-radius: 5px;
                font-weight: 500;
            ">
                {obj.role}
            </span>
        """)

    styled_role.short_description = "Role"

        
    


class PermissionAdmin(ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class GroupAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    autocomplete_fields = ("permissions",)


class SmsConfirmAdmin(ModelAdmin):
    list_display = ["phone", "code", "resend_count", "try_count"]
    search_fields = ["phone", "code"]
