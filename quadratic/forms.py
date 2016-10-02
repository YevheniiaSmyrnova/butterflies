# -*- coding: utf-8 -*-
'''
Quadratic forms module
'''
from django import forms


class QuadraticForm(forms.Form):
    '''
    Form for quadratic
    '''
    a = forms.FloatField(label=u'Коэффициент a', initial=1)
    b = forms.FloatField(label=u'Коэффициент b', initial=0)
    c = forms.FloatField(label=u'Коэффициент c', initial=0)

    def clean_a(self):
        '''
        Check coefficient a
        :return: a or Validation Error
        '''
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError(
                "коэффициент при первом слагаемом"
                " уравнения не может быть равным нулю")
        return self.cleaned_data['a']
