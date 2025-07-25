from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel




class MessagesModel(AbstractBaseModel):
    first_name = models.CharField(verbose_name=_("Ism"), max_length=255)
    phone = models.CharField(verbose_name=_("Telefon"), max_length=200)
    message = models.TextField(verbose_name=_("Xabar"), max_length=200)

    def __str__(self):
        return str(self.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )
        
    class Meta:
        db_table = "messages"
        verbose_name = _("MessagesModel")
        verbose_name_plural = _("MessagesModels")
