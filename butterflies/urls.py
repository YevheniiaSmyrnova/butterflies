from django.conf.urls import patterns, include, url, handler404
from django.contrib import admin
from butterflies.views import NewsView, IndexView, ContactView
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
	url(r'^news/$', NewsView.as_view(), name='news'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^collector/', include('collector.urls', namespace="collector")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^feedback/', include('feedbacks.urls', namespace="feedback")),
    url(r'^exhibition/', include('exhibition.urls', namespace="exhibition")),
    url(r'^sponsor/', include('sponsors.urls', namespace="sponsor")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)


