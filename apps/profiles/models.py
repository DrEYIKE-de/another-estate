from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampedUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    Male = "Male", _("Male")
    Female = "Female", _("Female")
    Other = "Other", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE,
    )
    phone_number = PhoneNumberField(
        default="+237690657643", verbose_name=_("Phone_number"), max_length=30
    )
    about_me = models.TextField(
        verbose_name=_("about me"), default=(" Say something about you")
    )
    license = models.CharField(
        max_length=20, verbose_name=_("License"), null=True, blank=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile photo"), upload_to="images/default_photo.jpeg"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.Other,
        max_length=30,
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        help_text=_("are you a buyer"),
        default=False,
    )
    is_seller = models.BooleanField(
        verbose_name=_("seller"),
        help_text=_("are you a seller"),
        default=False,
    )
    is_agent = models.BooleanField(
        verbose_name=_("agent"),
        help_text=_("are you a agent"),
        default=False,
    )
    country = CountryField(
        verbose_name=_("country name"),
        default="CM",
        max_length=255,
    )
    city = models.CharField(
        verbose_name=_("city"),
        default=("Douala"),
        max_length=100,
    )
    top_agent = models.BooleanField(
        verbose_name=_("Top Agent"),
        default=False,
    )
    ratings = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    num_reviews = models.IntegerField(
        verbose_name=_("Number of reviews"),
        default=0,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.user.username}"
