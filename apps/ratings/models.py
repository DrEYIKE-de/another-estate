from django.db import models
from django.utils.translation import gettext_lazy as _
from estate.settings.base import AUTH_USER_MODEL
from apps.profiles.models import Profile
from apps.common.models import TimeStampedUUIDModel


class Rating(TimeStampedUUIDModel):
    class Range(models.TextChoices):
        Range_1 = 1, _("Poor")
        Range_2 = 2, _("Fair")
        Range_3 = 3, _("Good")
        Range_4 = 4, _("Very Good")
        Range_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("The user who rating the agent"),
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("the rating agent"),
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        default=0,
        verbose_name=_("rating"),
        choices=Range.choices,
        help_text=_("1=Poor, 2=Fair, 3=Good, 4=Very Good, 5= Excellent"),
    )
    comments = models.TextField(verbose_name=_("users's comments"))

    class Meta:
        unique_together = ["agent", "rater"]

    def __str__(self):
        return f"{self.agent} rated at {self.rating} "
