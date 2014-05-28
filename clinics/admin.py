__author__ = 'mwalker'

from django.contrib import admin

from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from .models import Clinic


class ClinicsAdmin(admin.ModelAdmin, FrontendEditableAdminMixin):

    list_filter = ('region',)
    ordering = ('name',)


admin.site.register(Clinic, ClinicsAdmin)
