"""
Collector api urls module
"""
from django.conf.urls import patterns, url
from collector.api.views import CollectorListCreateAPIView, \
    CollectorRetrieveUpdateDestroyAPIView

urlpatterns = patterns(
    '',
    url(r'^$', CollectorListCreateAPIView.as_view(),
        name='collectors_list'),
    url(r'^(?P<pk>\d+)/$',
        CollectorRetrieveUpdateDestroyAPIView.as_view(),
        name='collector_detail'),
)
