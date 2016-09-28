from django.conf.urls import patterns, include, url, handler404
from django.contrib import admin
from butterflies.views import contact, news
from exhibition.views import list_of_exhibition
from django.http import HttpResponse
from django.shortcuts import render


urlpatterns = patterns('',
	url(r'news/$', news, name='news'),
    url(r'^$', list_of_exhibition, name='index'),
    url(r'^collector/', include('collector.urls', namespace="collector")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/$', contact, name='contact'),
    url(r'^feedback/', include('feedbacks.urls', namespace="feedback")),
    url(r'^exhibition/', include('exhibition.urls', namespace="exhibition")),
    url(r'^sponsor/', include('sponsors.urls', namespace="sponsor")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
)


