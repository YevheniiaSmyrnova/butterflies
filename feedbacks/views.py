# -*- coding: utf-8 -*-
'''
Feedbacks views module
'''
from django.contrib import messages
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView

from feedbacks.models import Feedback


class FeedbackCreateView(CreateView):
    '''
    Add new message
    '''
    model = Feedback
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        '''
        Send message
        :param form:
        :return: message
        '''
        data = form.cleaned_data
        mail_admins(data['subject'], data['message'], fail_silently=False,
                    connection=None,
                    html_message=None)
        message = super(FeedbackCreateView, self).form_valid(form)
        mes = u'Сообщение успешно отправленно.'
        messages.success(self.request, mes)
        return message
