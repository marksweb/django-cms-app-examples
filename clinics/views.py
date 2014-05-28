__author__ = 'mwalker'

from django.db.models import F
from django.shortcuts import (
    render_to_response, get_object_or_404, HttpResponseRedirect
)
from django.template import RequestContext

from .models import Clinic


def index(request):
    """
    Display the injury clinics by tier in random order.

    @param request: HttpRequest
    @rtype: HttpRedirect
    @return: Redirect to a default country filter
    """
    clinics = Clinic.objects.all().order_by('?')
    regions = Clinic.objects.values_list('region').distinct()

    tier_1 = clinics.filter(tier=1)
    tier_2 = clinics.filter(tier=2)
    tier_3 = clinics.filter(tier=3)

    return render_to_response(
        'clinics.html',
        RequestContext(
            request, {
                'regions': regions,
                'tier_1': tier_1,
                'tier_2': tier_2,
                'tier_3': tier_3
            }
        )
    )


def redirect(request, clinic_id=None):
    """
    View to store the click and then redirect to the charity URL.

    @param request: HttpRequest
    @type clinic_id: int
    @param clinic_id: the id of the selected clinic
    @return: HttpResponseRedirect
    """
    obj = get_object_or_404(Clinic, pk=clinic_id)
    # save click for the current clinic
    obj.clicks = F('clicks') + 1
    obj.save()

    return HttpResponseRedirect(obj.url)


def filter_clinics(request, filter_term=None):
    """
    Returns the clinics for the selected region.

    @param request: HttpRequest
    @type filter_term: unicode
    @param filter_term: Region selected
    @rtype: HttpResponse
    @return: listings filtered by selected country
    """
    clinics = Clinic.objects.filter(region=filter_term).order_by('?')

    tier_1 = clinics.filter(tier=1)
    tier_2 = clinics.filter(tier=2)
    tier_3 = clinics.filter(tier=3)

    return render_to_response(
        'clinics.html',
        RequestContext(
            request, {
                'tier_1': tier_1,
                'tier_2': tier_2,
                'tier_3': tier_3
            }
        )
    )