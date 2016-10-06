"""
Main urls module
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from butterflies.views import IndexView, FactsView, PoemsView, ContactView, \
    RegisterFormView, LoginFormView, LogoutView

urlpatterns = patterns(
    '',
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^facts/$', FactsView.as_view(), name='facts'),
    url(r'^poems/$', PoemsView.as_view(), name='poems'),
    url(r'^exhibition/', include('exhibition.urls', namespace="exhibition")),
    url(r'^sponsor/', include('sponsors.urls', namespace="sponsor")),
    url(r'^collector/', include('collector.urls', namespace="collector")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^feedback/', include('feedbacks.urls', namespace="feedback")),
    url(r'^quadratic/', include('quadratic.urls', namespace="quadratic")),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
