# -*- coding: utf-8 -*-
'''
Polls views module
'''
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from polls.models import Choice, Question


class IndexView(generic.ListView):
    '''
    List of question
    '''
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions
        """
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    '''
    Detail about question
    '''
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    '''
    Results of poll
    '''
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    '''
    Count of votes
    :param request:
    :param question_id:
    :return: count of votes or error message
    '''
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "Выберите один из варианов.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
