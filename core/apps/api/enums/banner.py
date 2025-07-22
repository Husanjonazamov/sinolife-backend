from django.utils.translation import gettext_lazy as _
from django.db import models

class BannerTypeChoice(models.TextChoices):
    HOME = "home", _("Bosh sahifa")
    ABOUT = "about", _("Biz haqimizda")
    PRODUCTS = "products", _("Mahsulotlar")
    CATEGORY = "category", _("Kategoriyalar")
    CONTACT = "contact", _("Aloqa")
