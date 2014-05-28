__author__ = 'mwalker'

from django.conf.urls import *


urlpatterns = patterns('clinics.views',
    url(r'^(?P<filter_term>[a-zA-Z]+)/$', 'filter_clinics', name='filter_clinics'),
    url(r'^redirect/(?P<clinic_id>\d+)/$', 'redirect', name='redirect'),
    url(r'^$', 'index', name='injury_clinics'),
)
