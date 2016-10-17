"""
Main urls module
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

from collector.api import urls as collector_api_url
from exhibition.api import urls as exhibition_api_url
from sponsors.api import urls as sponsors_api_url
from butterflies.views import IndexView, FactsView, PoemsView, ContactView, \
    RegisterCreateView

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = patterns(
    '',
    url(r'^api/collectors/', include(collector_api_url,
                                     namespace="collector_api_url")),
    url(r'^api/exhibitions/', include(exhibition_api_url,
                                      namespace="exhibition_api_url")),
    url(r'^api/', include(sponsors_api_url,namespace="sponsors_api_url")),
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
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
