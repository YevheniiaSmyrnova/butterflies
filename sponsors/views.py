# -*- coding: utf-8 -*-
# TODO doc string
from django.shortcuts import render

from sponsors.models import Sponsor


def list_of_sponsor(request):
    # TODO doc string
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsors/list.html', {'sponsors': sponsors})


def detail(request, num):
    # TODO doc string
    # TODO check this magic
    num = num
    sponsor = Sponsor.objects.get(id=num)
    return render(request, 'sponsors/detail.html', {'sponsor': sponsor})
