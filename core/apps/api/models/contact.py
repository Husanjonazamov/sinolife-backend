from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ContactModel(AbstractBaseModel):
    phone = models.CharField(verbose_name=_("Telefon"), max_length=200)
    address = models.TextField(verbose_name=_("Manzil"))
    telegram = models.URLField(verbose_name=_("Telegram"), help_text="Misol: https://t.me/username")

    def __str__(self):
        return str(self.phone)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "contact"
        verbose_name = _("ContactModel")
        verbose_name_plural = _("ContactModels")
