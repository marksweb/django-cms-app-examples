__author__ = 'mwalker'

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

from django.utils.translation import ugettext_lazy as _


class ClinicsApphook(CMSApp):
    name = _("Injury Clinics App")
    urls = ["clinics.urls"]
    app_name = "clinics"

apphook_pool.register(ClinicsApphook)