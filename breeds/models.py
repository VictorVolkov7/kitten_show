from django.db import models
from django.utils.translation import gettext_lazy as _


class Breed(models.Model):
    """Base breed model."""

    breed_name = models.CharField(
        max_length=155,
        verbose_name=_("Breed"),
    )
    description = models.TextField(
        verbose_name=_("Breed description"),
    )

    def __str__(self):
        """
        String representation of Breed model.

        Uses the model breed_name field.
        """
        return self.breed_name

    class Meta:
        verbose_name = _("Breed")
        verbose_name_plural = _("Breeds")
