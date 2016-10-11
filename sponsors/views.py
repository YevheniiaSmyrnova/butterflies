# -*- coding: utf-8 -*-
"""
Sponsops views module
"""
from django.views.generic.detail import DetailView

from sponsors.models import Sponsor


class SponsorDetailView(DetailView):
    """
    Detail about sponsor
    """
    model = Sponsor
