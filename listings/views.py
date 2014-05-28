__author__ = 'mwalker'

from django.core.urlresolvers import reverse
from django.db.models import F, Q
from django.shortcuts import (
    render_to_response, get_object_or_404, HttpResponseRedirect
)
from django.template import RequestContext
from django.utils import timezone

from .models import Listing, Tracking, COUNTRY_CHOICES


def index(request):
    """
    Redirect to the country filtered listings.

    @param request: HttpRequest
    @rtype: HttpRedirect
    @return: Redirect to a default country filter
    """
    return HttpResponseRedirect(
        reverse(
            'listings:filter_listings',
            kwargs={
                "filter_term": 'UK'
            }
        )
    )


def redirect(request, charity_id=None):
    """
    View to store the click and then redirect to the charity URL.

    @param request: HttpRequest
    @type charity_id: int
    @param charity_id: the id of the selected charity
    @return: HttpResponseRedirect
    """
    charity = get_object_or_404(Listing, pk=charity_id)
    year = charity.end_date.year
    obj, created = Tracking.objects.get_or_create(listing=charity, year=year)
    tracking = obj or created
    # save click for the current listing
    charity.clicks = F('clicks') + 1
    charity.save()
    # save click for year total
    tracking.clicks = F('clicks') + 1
    tracking.save()

    return HttpResponseRedirect(charity.charity_url)


def filter_listings(request, filter_term=None):
    """
    Returns the charity listings for the selected country.

    @param request: HttpRequest
    @type filter_term: unicode
    @param filter_term: Country or Letter selected
    @rtype: HttpResponse
    @return: listings filtered by selected country
    """
    now = timezone.now()

    if any(filter_term in country for country in COUNTRY_CHOICES):
        # Country filter
        filtered_listings = Listing.objects.filter(
            country=filter_term,
            start_date__lte=now, end_date__gte=now
        ).exclude(disabled=True).order_by('?')
    else:
        # A-Z filter
        filtered_listings = Listing.objects.filter(
            Q(category=5) | Q(category=7),
            charity_name__istartswith=filter_term,
            start_date__lte=now, end_date__gte=now
        ).exclude(disabled=True).order_by('?')

    tier_1 = filtered_listings.filter(tier=1)
    tier_2 = filtered_listings.filter(tier=2)
    tier_3 = filtered_listings.filter(tier=3)

    return render_to_response('listings.html',
        RequestContext(
            request, {
                'tier_1': tier_1,
                'tier_2': tier_2,
                'tier_3': tier_3
            }
        )
    )
