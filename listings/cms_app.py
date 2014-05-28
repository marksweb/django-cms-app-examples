__author__ = 'mwalker'

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class ListingsApphook(CMSApp):
    name = _("Charity Listings App")
    urls = [
        "listings.urls"
    ]
    app_name = "listings"

apphook_pool.register(ListingsApphook)