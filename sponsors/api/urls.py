from django.conf.urls import patterns, url
from sponsors.api.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = patterns(
    '',
    url(r'^users/$', UserListCreateAPIView.as_view(),
        name='users_list'),
    url(r'^users/(?P<id>[0-9]+)/$', UserRetrieveUpdateDestroyAPIView.as_view()),
)