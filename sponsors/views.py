# -*- coding: utf-8 -*-
'''
Sponsops views module
'''
from django.shortcuts import render

from sponsors.models import Sponsor

# TODO make class
def list_of_sponsor(request):
    '''
    List of sponsor
    :param request:
    :return:
    '''
    sponsors = Sponsor.objects.all()
    return render(request, 'sponsors/list.html', {'sponsors': sponsors})


def detail(request, pk):
    '''
    Detain of sponsor
    :param request:
    :param pk:
    :return:
    '''
    sponsor = Sponsor.objects.get(id=pk)
    return render(request, 'sponsors/detail.html', {'sponsor': sponsor})
