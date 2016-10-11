"""
Collector urls module
"""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from collector.views import CollectorListView, CollectorDetailView, \
    CollectorCreateView, CollectorUpdateView, CollectorDeleteView, \
    add_collection

urlpatterns = patterns(
    '',
    url(r'^$', CollectorListView.as_view(), name='list'),
    url(r'^add/$',
        login_required(CollectorCreateView.as_view()), name='create'),
    url(r'^edit/(?P<pk>\w+)/$',
        login_required(CollectorUpdateView.as_view()), name='edit'),
    url(r'^delete/(?P<pk>\w+)/$',
        login_required(CollectorDeleteView.as_view()), name='delete'),
    url(r'^detail/(?P<pk>\w+)/$',
        CollectorDetailView.as_view(), name='detail'),
    url(r'^add-collection/(?P<pk>\w+)/$', login_required(add_collection),
        name='add_collection'),
)
