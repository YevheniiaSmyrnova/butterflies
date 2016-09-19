# -*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor

# Create your views here.
def list_of_exhibition(request):
	exhibitions = Exhibition.objects.all()
	exhibit = []
	for exhibition in exhibitions:
		if exhibition.date.year > datetime.now().year:
			exhibit.append(exhibition)
		if exhibition.date.month > datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibit.append(exhibition)
		if exhibition.date.day >= datetime.now().day and exhibition.date.month == datetime.now().month and exhibition.date.year == datetime.now().year:
			exhibit.append(exhibition)
	return render(request, 'index.html', {'exhibitions': exhibit})

def detail(request, num):
	num=num
	exhibition = Exhibition.objects.get(id=num)
	#collection = Collection.objects.values('name').get(exhibition__id=num)
	collection = Collection.objects.get(exhibition__id=num)
	sponsor = Sponsor.objects.get(sponsor_exhibition__id=num)
	assistant = Sponsor.objects.get(assistant_exhibition__id=num)
	return render(request, 'exhibition/detail.html', {'exhibition': exhibition, 'collection': collection, 'sponsor': sponsor, 'assistant': assistant})
