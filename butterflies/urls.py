from django.conf.urls import patterns, include, url, handler404
from django.contrib import admin
from butterflies.views import IndexView, FactsView, PoemsView, ContactView
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^facts/$', FactsView.as_view(), name='facts'),
    url(r'^poems/$', PoemsView.as_view(), name='poems'),
    url(r'^collector/', include('collector.urls', namespace="collector")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^feedback/', include('feedbacks.urls', namespace="feedback")),
    url(r'^exhibition/', include('exhibition.urls', namespace="exhibition")),
    url(r'^sponsor/', include('sponsors.urls', namespace="sponsor")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)


