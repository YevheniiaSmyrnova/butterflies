"""
Collector api urls module
"""
from django.conf.urls import patterns, url
from collector.api.views import CollectorListCreateAPIView, \
    CollectorRetrieveUpdateDestroyAPIView

urlpatterns = patterns(
    '',
    url(r'^collectors/$', CollectorListCreateAPIView.as_view(),
        name='collectors_list'),
    url(r'^collectors/(?P<pk>\d+)/$',
        CollectorRetrieveUpdateDestroyAPIView.as_view(),
        name='collector_detail'),
)
