'''
Collector urls module
'''
from django.conf.urls import patterns, url

from collector.views import CollectorListView, CollectorDetailView, \
    CollectorCreateView, CollectorUpdateView, CollectorDeleteView, \
    add_collection

urlpatterns = patterns(
    '',
    url(r'^$', CollectorListView.as_view(), name='list'),
    url(r'^add/$', CollectorCreateView.as_view(),
        name='create'),
    url(r'^edit/(?P<pk>\w+)/$',
        CollectorUpdateView.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\w+)/$',
        CollectorDeleteView.as_view(), name='delete'),
    url(r'^detail/(?P<pk>\w+)/$',
        CollectorDetailView.as_view(), name='detail'),
    url(r'^add-collection/(?P<pk>\w+)/$', add_collection,
        name='add_collection'),
)
