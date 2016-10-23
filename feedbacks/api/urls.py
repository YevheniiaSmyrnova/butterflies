"""
Feedback api urls module
"""
from django.conf.urls import patterns, url
from feedbacks.api.views import FeedbackListCreateAPIView, \
    FeedbackRetrieveUpdateDestroyAPIView


urlpatterns = patterns(
    '',
    url(r'^feedback/$', FeedbackListCreateAPIView.as_view(),
        name='feedbacks_list'),
    url(r'^feedback/(?P<pk>\d+)/$', FeedbackRetrieveUpdateDestroyAPIView.as_view(),
        name='feedback_detail'),
)
