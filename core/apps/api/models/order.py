from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.enums.order import OrderPaymentChoice, OrderStatusChoice, OrderPaymentStatusChoice



class OrderModel(AbstractBaseModel):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="order"
    )
    
    first_name = models.CharField(verbose_name=_("Ism"), max_length=200, blank=True, null=True)
    phone = models.CharField(verbose_name=_("Telefon"), max_length=30, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    payment_type = models.CharField(
        verbose_name=_("To'lov turi"),
        max_length=30,
        choices=OrderPaymentChoice.choices,
        default=OrderPaymentChoice.CLICK
    )
    status = models.CharField(verbose_name=_("Status"), max_length=200, choices=OrderStatusChoice.choices, default=OrderStatusChoice.PENDING)
    payment_status = models.CharField(verbose_name=_("Tolov statusi"), max_length=200, choices=OrderPaymentStatusChoice.choices, default=OrderPaymentStatusChoice.UNPAID)
    
    total = models.DecimalField(
        verbose_name=_("Jami narx"),
        max_digits=30, decimal_places=2
    )
    pay_link = models.URLField(null=True, blank=True)

    

    def __str__(self):
        return str(self.user.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")



class OrderitemModel(AbstractBaseModel):
    order = models.ForeignKey(
        OrderModel,
        on_delete=models.CASCADE,
        related_name="order_items"
    )
    product = models.ForeignKey(
        "api.ProductModel",
        on_delete=models.CASCADE,
        verbose_name=_("Mahsulot")
    )
    quantity = models.PositiveIntegerField(verbose_name=_("Soni"), default=1)
    total_price = models.DecimalField(
        verbose_name=_("jami narx"),
        max_digits=15, 
        decimal_places=2
    )
    

    def __str__(self):
        return str(self.product.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "orderItem"
        verbose_name = _("OrderitemModel")
        verbose_name_plural = _("OrderitemModels")
