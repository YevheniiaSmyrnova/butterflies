"""
Main urls module
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

from collector.api import urls as collector_api_urls
from exhibition.api import urls as exhibition_api_urls
from feedbacks.api import urls as feedback_api_urls
from polls.api import urls as poll_api_urls
from sponsors.api import urls as sponsors_api_urls
from butterflies.views import IndexView, FactsView, PoemsView, ContactView, \
    RegisterCreateView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = patterns(
    '',
    url(r'^api/login/$', obtain_auth_token),
    url(r'^api/', include(collector_api_urls, namespace="collector_api_urls")),
    url(r'^api/', include(exhibition_api_urls, namespace="exhibition_api_urls")),
    url(r'^api/', include(feedback_api_urls, namespace="feedback_api_urls")),
    url(r'^api/', include(poll_api_urls, namespace="poll_api_urls")),
    url(r'^api/', include(sponsors_api_urls, namespace="sponsors_api_urls")),
    url(r'^register/$', RegisterCreateView.as_view(), name='register'),
    url(r'^login/$', login, {"template_name": "login.html"}, name='login'),
    url(r'^logout/$', logout, {"template_name": "logout.html"}, name='logout'),
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

