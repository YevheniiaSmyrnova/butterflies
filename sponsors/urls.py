'''
Sponsors urls module
'''
from django.conf.urls import patterns, url

from sponsors.views import detail

urlpatterns = patterns(
    '',
    url(r'^(?P<pk>\w+)/$', detail, name='detail'),
)
