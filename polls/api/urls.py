"""
Polls api urls module
"""
from django.conf.urls import patterns, url
from polls.api.views import QuestionListCreateAPIView, \
    QuestionRetrieveUpdateDestroyAPIView, ChoiceListCreateAPIView

urlpatterns = patterns(
    '',
    url(r'^$', QuestionListCreateAPIView.as_view(),
        name='questions_list'),
    url(r'^(?P<pk>\d+)/$', QuestionRetrieveUpdateDestroyAPIView.as_view(),
        name='question_detail'),
    url(r'^(?P<pk>\d+)/choices/$', ChoiceListCreateAPIView.as_view(),
        name='choices_list'),
)
