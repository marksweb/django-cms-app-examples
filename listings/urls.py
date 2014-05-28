__author__ = 'mwalker'

from django.conf.urls import *


urlpatterns = patterns('listings.views',
    url(r'^(?P<filter_term>[a-zA-Z]+)/$', 'filter_listings', name='filter_listings'),
    url(r'^redirect/(?P<charity_id>\d+)/$', 'redirect', name='redirect_listings'),
    url(r'^$', 'index', name='charity_listings'),
)
