"""
Polls api urls module
"""
from django.conf.urls import patterns, url
from polls.api.views import QuestionListCreateAPIView, \
    ExhibitionRetrieveUpdateDestroyAPIView


urlpatterns = patterns(
    '',
    url(r'^$', QuestionListCreateAPIView.as_view(),
        name='questions_list'),
    url(r'^(?P<pk>\d+)/$', ExhibitionRetrieveUpdateDestroyAPIView.as_view(),
        name='question_detail'),
)
