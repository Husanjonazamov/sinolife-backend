from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderPaymentChoice(models.TextChoices):
    CLICK = "click", _("Click")
    PAYME = "payme", _("Payme")