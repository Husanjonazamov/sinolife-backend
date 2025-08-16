from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ProductimageModel, ProductModel


@receiver(post_save, sender=ProductModel)
def ProductSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=ProductimageModel)
def ProductimageSignal(sender, instance, created, **kwargs): ...
