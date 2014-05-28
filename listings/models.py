__author__ = 'mwalker'

# from dateutil.relativedelta import relativedelta

from django.db import models
from django.utils.translation import gettext as _


AUS = 'AUS'
NZ = 'NZ'
UK = 'UK'
USA = 'USA'
COUNTRY_CHOICES = (
    (AUS, _("Australia")),
    (NZ, _("New Zealand")),
    (UK, _("United Kingdom")),
    (USA, _("United States")),
)
CATEGORY_CHOICES = (
    (1, 'UK'),
    (2, 'US'),
    (3, 'AU'),
    (4, 'NZ'),
    (5, 'A-Z'),
    (6, 'Ballot'),
    (7, 'Ballot A-Z'),
)
MONTHS_6 = 6
MONTHS_9 = 9
MONTHS_12 = 12
MONTHS_15 = 15
MONTHS_18 = 18
MONTHS_21 = 21
MONTHS_24 = 24
DURATION_CHOICES = (
    (MONTHS_6, _('6 Months')),
    (MONTHS_9, _('9 Months')),
    (MONTHS_12, _('12 Months')),
    (MONTHS_15, _('15 Months')),
    (MONTHS_18, _('18 Months')),
    (MONTHS_21, _('21 Months')),
    (MONTHS_24, _('24 Months')),
)
TIER_CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3)
)


class Listing(models.Model):
    """
    Model for storing a charity listing.
    """
    tier = models.IntegerField(
        _("Tier"),
        max_length=1,
        blank=False,
        null=False,
        choices=TIER_CHOICES
    )
    start_date = models.DateTimeField(
        _("Start date"),
        auto_now=False,
    )
    end_date = models.DateTimeField(
        _("End date"),
        auto_now=False,
        editable=False
    )
    country = models.CharField(
        _("Country"),
        choices=COUNTRY_CHOICES,
        max_length=50
    )
    charity_name = models.CharField(
        _("Charity name"),
        max_length=255,
    )
    charity_desc = models.TextField(
        _("Charity description")
    )
    contact_name = models.CharField(
        _("Contact name"),
        max_length=255,
    )
    contact_email = models.EmailField(
        _("Contact email")
    )
    contact_phone = models.CharField(
        _("Contact telephone"),
        max_length=30,
    )
    charity_url = models.URLField(
        _("Website")
    )
    clicks = models.IntegerField(
        _("Clicks"),
        default=0,
        blank=True,
        null=True,
    )
    category = models.IntegerField(
        _("Category"),
        choices=CATEGORY_CHOICES,
    )
    duration = models.IntegerField(
        _("Duration"),
        choices=DURATION_CHOICES,
    )
    disabled = models.BooleanField(
        _("Disabled"),
        default=False
    )

    class Meta:
        verbose_name = _("Charity listing")
        db_table = 'charity_listings'

    # def clean(self, *args, **kwargs):
    #     """
    #     Force the end date based on the start date and duration when we save
    #     a listing.
    #     """
    #     self.end_date = self.start_date + relativedelta(months=self.duration)
    #     super(Listing, self).clean(*args, **kwargs)

    def __unicode__(self):
        return self.charity_name

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


class Tracking(models.Model):
    """
    Model to track clicks by year on the listings.
    """
    listing = models.ForeignKey(Listing)
    year = models.IntegerField()
    clicks = models.IntegerField(default=0)

    def __unicode__(self):
        return '{charity} has received {clicks} clicks during {year}'.format(
            charity=self.listing,
            year=self.year,
            clicks=self.clicks
        )

    class Meta:
        verbose_name = _("Charity listing tracking")
        verbose_name_plural = _("Charity listing tracking details")
        db_table = 'charity_listings_tracking'
