# -*- coding: utf-8 -*-
# TODO doc string
from django import forms

from exhibition.models import Exhibition


class ExhibitionModelForm(forms.ModelForm):
    # TODO doc string
    class Meta:
        # TODO doc string
        model = Exhibition
