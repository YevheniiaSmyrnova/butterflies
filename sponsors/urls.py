"""
Sponsors urls module
"""
from django.conf.urls import patterns, url

from sponsors.views import SponsorDetailView

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\w+)/$', SponsorDetailView.as_view(), name='detail'),
)
