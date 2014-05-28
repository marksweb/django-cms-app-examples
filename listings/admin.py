__author__ = 'mwalker'

from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from .models import Listing, Tracking


class ListingsAdmin(admin.ModelAdmin, FrontendEditableAdminMixin):

    list_filter = ('category', 'country', 'tier')
    ordering = ('-end_date',)

    readonly_fields = ('end_date',)

    class Media:
        """
        Allow for custom javascript showing the end date calculation.
        """
        js = ("js/listings.js",)


class ListingsTrackingAdmin(admin.ModelAdmin, FrontendEditableAdminMixin):
    list_filter = ('year',)
    ordering = ('-clicks',)


admin.site.register(Listing, ListingsAdmin)
admin.site.register(Tracking, ListingsTrackingAdmin)
