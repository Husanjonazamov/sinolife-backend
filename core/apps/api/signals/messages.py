from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import MessagesModel


@receiver(post_save, sender=MessagesModel)
def MessagesSignal(sender, instance, created, **kwargs): ...
