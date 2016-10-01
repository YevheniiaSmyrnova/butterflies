# TODO doc string
from django.conf.urls import patterns, url

from sponsors.views import detail

urlpatterns = patterns(
    '',
    # TODO don't keep unnecessary comments
    # url(r'^$', list_of_sponsor, name='list'),
    url(r'^(?P<num>\w+)/$', detail, name='detail'),
)
