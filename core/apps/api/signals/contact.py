from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import ContactModel


@receiver(post_save, sender=ContactModel)
def ContactSignal(sender, instance, created, **kwargs): ...
