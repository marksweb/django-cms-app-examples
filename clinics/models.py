__author__ = 'mwalker'

from dateutil.relativedelta import relativedelta

from django.db import models
from django.utils.translation import gettext as _


TIER_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3)
)


class Clinic(models.Model):
    """
    Model for storing a clinic.
    """
    name = models.CharField(
        _("Charity name"),
        max_length=255,
    )
    email = models.EmailField(
        _("Email")
    )
    specialism = models.CharField(
        _("Specialism"),
        max_length=255,
    )
    desc = models.TextField(
        _("Charity description")
    )
    address_1 = models.CharField(
        _("Address line 1"),
        max_length=255,
    )
    address_2 = models.CharField(
        _("Address line 2"),
        max_length=255,
    )
    town = models.CharField(
        _("Town"),
        max_length=100,
    )
    county = models.CharField(
        _("County"),
        max_length=50
    )
    postcode = models.CharField(
        _("Postcode"),
        max_length=12,
    )
    phone = models.CharField(
        _("Contact telephone"),
        max_length=30,
    )
    url = models.URLField(
        _("Website")
    )
    region = models.CharField(
        _("Region"),
        max_length=255,
    )
    clicks = models.IntegerField(
        _("Clicks"),
        default=0,
        blank=True,
        null=True,
    )
    tier = models.IntegerField(
        _("Tier"),
        max_length=1,
        blank=False,
        null=False,
        choices=TIER_CHOICES
    )

    class Meta:
        verbose_name = _("Injury clinic")
        db_table = 'injury_clinics'

    def __unicode__(self):
        return self.name

    def display_class(self):
        """
        Helper to display the CSS class in the template based on the set tier.

        @rtype: str
        @return: CSS class for the template
        """
        class_lookup = {
            1: "tier1",
            2: "tier2",
            3: "tier3",
        }
        return class_lookup[self.tier]
