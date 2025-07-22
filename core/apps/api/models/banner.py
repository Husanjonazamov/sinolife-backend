from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.banner import BannerTypeChoice


class BannerModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=200, blank=True, null=True)
    subtitle = models.CharField(verbose_name=_("Kichik Sarlavha"), max_length=300, blank=True, null=True)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    type = models.CharField(verbose_name=_("Sahifa"), max_length=200, choices=BannerTypeChoice.choices, default=BannerTypeChoice.HOME)
    image = models.ImageField(
        _("Image"),
        upload_to="banners/",
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")
