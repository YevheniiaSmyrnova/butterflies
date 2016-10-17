# -*- coding: utf-8 -*-
"""
Collector forms module
"""
from django import forms

from collector.models import Collector
from exhibition.models import Collection


class CollectorModelForm(forms.ModelForm):
    """
    Collector form
    """
    class Meta:
        """
        Meta params
        """
        model = Collector
        exclude = tuple()


class CollectionModelForm(forms.ModelForm):
    """
    Collection form
    """
    class Meta:
        """
        Meta params
        """
        model = Collection
        exclude = tuple()
