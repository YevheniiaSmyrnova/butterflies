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


'''def detail(request, pk):
    sponsor = Sponsor.objects.get(id=pk)
    return render(request, 'sponsors/detail.html', {'sponsor': sponsor})'''
