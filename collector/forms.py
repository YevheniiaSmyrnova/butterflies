# -*- coding: utf-8 -*-
# TODO doc string
from django import forms

from collector.models import Collector
from exhibition.models import Collection


# Create your views here.
class CollectorModelForm(forms.ModelForm):
    # TODO doc string
    class Meta:
        # TODO doc string
        model = Collector

        fieldsets = [
            (u'Основная информация',
             ['name', 'surname', 'date_of_birth', 'photo']),
            (u'Контактная информация', ['email', 'phone', 'address', 'skype']),
        ]


class CollectionModelForm(forms.ModelForm):
    # TODO doc string
    class Meta:
        # TODO doc string
        model = Collection
