# -*- coding: utf-8 -*-
"""
Exhibiton forms module
"""
from django import forms

from exhibition.models import Exhibition


class ExhibitionModelForm(forms.ModelForm):
    """
    Exhibition form
    """
    class Meta:
        """
        Meta params
        """
        model = Exhibition
