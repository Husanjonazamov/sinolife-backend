from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CartModel(AbstractBaseModel):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="users",
    )    
    total_price = models.DecimalField(
        verbose_name=_("Jami narx"),
        max_digits=20, decimal_places=2
    )
    

    def __str__(self):
        return str(self.user.first_name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "cart"
        verbose_name = _("CartModel")
        verbose_name_plural = _("CartModels")




class CartitemModel(AbstractBaseModel):
    cart = models.ForeignKey(
        CartModel,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )
    product = models.ForeignKey(
        "api.ProductModel",
        on_delete=models.CASCADE,
        related_name="product"
    )
    quantity = models.PositiveIntegerField(
        verbose_name=_("Soni"),
        default=0
    )
    total_price = models.DecimalField(
        verbose_name=_("Jami narx"),
        max_digits=20, decimal_places=2
    )
    
    

    def __str__(self):
        return str(self.product.title)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "cartItem"
        verbose_name = _("CartitemModel")
        verbose_name_plural = _("CartitemModels")
