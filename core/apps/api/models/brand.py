from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BrandModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    image = models.ImageField(upload_to="brand/", blank=True, null=True)

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "brand"
        verbose_name = _("BrandModel")
        verbose_name_plural = _("BrandModels")
