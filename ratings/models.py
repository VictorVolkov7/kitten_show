from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from kittens.models import Kitten
from users.models import User


class Rating(models.Model):
    """Base rating model."""

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Rating"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="users_ratings",
        verbose_name=_("User"),
    )
    kitten = models.ForeignKey(
        Kitten,
        on_delete=models.CASCADE,
        related_name="kitten_ratings",
        verbose_name=_("Kitten"),
    )

    def __str__(self):
        """
        String representation of Rating model.

        Uses the model name, breed, age_year, age_month fields.
        """
        return (
            f"{self.rating} star{'s' if self.rating > 1 else ''}"
            f" for the {self.kitten.name} by {self.user.email}"
        )

    class Meta:
        verbose_name = _("Rating")
        verbose_name_plural = _("Ratings")
