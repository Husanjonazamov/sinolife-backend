from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class CommentModel(AbstractBaseModel):
    product = models.ForeignKey("api.ProductModel", on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    message = models.TextField()
    

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "comment"
        verbose_name = _("CommentModel")
        verbose_name_plural = _("CommentModels")
