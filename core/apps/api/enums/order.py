from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderPaymentChoice(models.TextChoices):
    CLICK = "click", _("Click")
    PAYME = "payme", _("Payme")
    CASH = "cash", _("Naqt pul")
    
    
class OrderStatusChoice(models.TextChoices):
    PENDING = 'pending', 'Kutilmoqda'
    ACCEPTED = 'accepted', 'Qabul qilindi'
    REJECTED = 'rejected', 'Rad etildi'
    COMPLETED = 'completed', 'Yakunlandi'
    
    
class OrderPaymentStatusChoice(models.TextChoices):
    PAID = 'paid', 'To‘landi'
    UNPAID = 'unpaid', 'To‘lanmadi'