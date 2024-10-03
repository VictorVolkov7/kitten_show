from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from breeds.models import Breed


class Kitten(models.Model):
    """Base kitten model."""

    name = models.CharField(
        max_length=255,
        verbose_name=_("Kitten name"),
    )
    age_year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        verbose_name=_("Age in year"),
    )
    age_month = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        verbose_name=_("Age in month"),
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        null=True,
        related_name="kittens_with_breed",
        verbose_name=_("Breed"),
    )
    color = models.CharField(
        max_length=155,
        verbose_name=_("Color"),
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Description"),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="kittens",
        verbose_name=_("Owner"),
    )

    def __str__(self):
        """
        String representation of Kitten model.

        Uses the model name, breed, age_year, age_month fields.
        """
        return (
            f"Kitten {self.name} of the {self.breed} breed, "
            f"{self.age_year} year and {self.age_month} month old."
        )

    class Meta:
        verbose_name = _("Kitten")
        verbose_name_plural = _("Kittens")
