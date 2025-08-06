from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.TextChoices):
    """
    User Role Choice
    """

    SUPERUSER = "superuser", _("Superuser")
    ADMIN = "admin", _("Admin")
    USER = "user", _("User")

class LangChoices(models.TextChoices):
    UZBEK = 'uz', 'Uzbek'
    ENGLISH = 'en', 'English'
    RUSSIAN = 'ru', 'Russian'
    

