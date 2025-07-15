from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ProductModel


@receiver(post_save, sender=ProductModel)
def ProductSignal(sender, instance, created, **kwargs): ...
