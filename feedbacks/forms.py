# -*- coding: utf-8 -*-
# TODO doc string
from django import forms

from feedbacks.models import Feedback


# Create your views here.
class FeedbackModelForm(forms.ModelForm):
    # TODO doc string
    class Meta:
        # TODO doc string
        model = Feedback
