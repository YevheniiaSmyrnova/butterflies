# -*- coding: utf-8 -*-
'''
Feedbacks forms module
'''
from django import forms

from feedbacks.models import Feedback


# Create your views here.
class FeedbackModelForm(forms.ModelForm):
    '''
    Feedback form
    '''
    class Meta:
        '''
        Meta params
        '''
        model = Feedback
