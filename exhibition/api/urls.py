"""
Exhibition api urls module
"""
from django.conf.urls import patterns, url
from exhibition.api.views import ExhibitionListCreateAPIView, \
    ExhibitionRetrieveUpdateDestroyAPIView, CollectionListCreateAPIView, \
    CollectionRetrieveUpdateDestroyAPIView

urlpatterns = patterns(
    '',
    url(r'^exhibitions/$', ExhibitionListCreateAPIView.as_view(),
        name='exhibitions_list'),
    url(r'^exhibitions/(?P<pk>\d+)/$', ExhibitionRetrieveUpdateDestroyAPIView.as_view(),
        name='exhibition_detail'),
    url(r'^collections/$', CollectionListCreateAPIView.as_view(),
        name='collections_list'),
    url(r'^collections/(?P<pk>\d+)/$',
        CollectionRetrieveUpdateDestroyAPIView.as_view(),
        name='collection_detail'),
)
