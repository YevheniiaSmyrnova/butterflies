# TODO doc string
from django.conf.urls import patterns, url

from feedbacks.views import FeedbackCreateView

urlpatterns = patterns(
    '',
    url(r'^$', FeedbackCreateView.as_view(), name='new_message'),
)
