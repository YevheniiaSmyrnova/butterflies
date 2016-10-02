# -*- coding: utf-8 -*-
'''
Collector forms module
'''
from django import forms

from collector.models import Collector
from exhibition.models import Collection


# Create your views here.
class CollectorModelForm(forms.ModelForm):
    '''
    Collector form
    '''
    class Meta:
        '''
        Meta params
        '''
        model = Collector


class CollectionModelForm(forms.ModelForm):
    '''
    Collection form
    '''
    class Meta:
        '''
        Meta params
        '''
        model = Collection
