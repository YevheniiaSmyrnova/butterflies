# -*- coding: utf-8 -*-
# TODO doc string
from django import forms


class QuadraticForm(forms.Form):
    # TODO doc string
    a = forms.FloatField(label=u'Коэффициент a', initial=1)
    b = forms.FloatField(label=u'Коэффициент b', initial=0)
    c = forms.FloatField(label=u'Коэффициент c', initial=0)

    def clean_a(self):
        # TODO doc string
        a = self.cleaned_data['a']
        if a == 0:
            raise forms.ValidationError(
                "коэффициент при первом слагаемом"
                " уравнения не может быть равным нулю")
        return self.cleaned_data['a']
