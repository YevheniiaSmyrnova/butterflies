"""
Exhibition urls module
"""
from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from exhibition.views import ExhibitionListView, ExhibitionPastListView, \
    ExhibitionDetailView, ExhibitionCreateView, ExhibitionUpdateView, \
    ExhibitionDeleteView

urlpatterns = patterns(
    '',
    url(r'^$', ExhibitionListView.as_view(), name='list'),
    url(r'^past/$', ExhibitionPastListView.as_view(), name='list_past'),
    url(r'^detail/(?P<pk>\w+)/$', ExhibitionDetailView.as_view(),
        name='detail'),
    url(r'^add/$', 
        login_required(ExhibitionCreateView.as_view()), name='create'),
    url(r'^edit/(?P<pk>\w+)/$', 
        login_required(ExhibitionUpdateView.as_view()), name='edit'),
    url(r'^delete/(?P<pk>\w+)/$', 
        login_required(ExhibitionDeleteView.as_view()), name='delete'),
)
