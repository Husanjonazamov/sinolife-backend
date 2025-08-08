from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ProductModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("Nomi"), max_length=255)
    description = models.TextField(verbose_name=_("Tavsif"), blank=True, null=True)
    category = models.ForeignKey(
        "api.CategoryModel",
        verbose_name=_("Kategoriya"),
        on_delete=models.CASCADE,
        related_name="products",
        blank=True,
        null=True,
    )
    discounted_price = models.DecimalField(
        verbose_name=_("Asl narx"), max_digits=10, decimal_places=2, blank=True, null=True
    )
    price = models.DecimalField(verbose_name=_("Chegirmadagi narx"), max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name=_("Rasm"), upload_to="products/", blank=True)
    quantity = models.PositiveIntegerField(verbose_name=_("Mahsulot soni"), default=0)
    
    is_populer = models.BooleanField(verbose_name=_("Mashhurmi ?"), default=False)
    is_new = models.BooleanField(verbose_name=_("Yangi mahsulotmi ?"), default=False)
    is_discounted = models.BooleanField(verbose_name=_("Chegirmada"), default=False)
    
    image_id = models.CharField(verbose_name=_("Bot Mahsulotidagi rasm"), max_length=200, blank=True, null=True)
    video_id = models.CharField(verbose_name=_("Bot Mahsulotidagi Video"), max_length=200, blank=True, null=True)
    
    

    def __str__(self):
        return str(self.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "product"
        verbose_name = _("ProductModel")
        verbose_name_plural = _("ProductModels")
