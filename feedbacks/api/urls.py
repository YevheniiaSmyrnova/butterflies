"""
Feedback api urls module
"""
from django.conf.urls import patterns, url
from feedbacks.api.views import FeedbackListCreateAPIView, \
    FeedbackRetrieveUpdateDestroyAPIView


urlpatterns = patterns(
    '',
    url(r'^$', FeedbackListCreateAPIView.as_view(),
        name='feedback_list'),
    url(r'^(?P<pk>\d+)/$', FeedbackRetrieveUpdateDestroyAPIView.as_view(),
        name='feedback_detail'),
)
