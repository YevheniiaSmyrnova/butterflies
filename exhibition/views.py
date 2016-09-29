# -*- coding: utf-8 -*-
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor
from exhibition.forms import ExhibitionModelForm
import logging
logger = logging.getLogger(__name__)

# Create your views here.

# def test(**kwargs): # {"name": "fff", "short_description": "bla", "description": "asda", "data": timezone.now()}
# 	for key, value in kwargs.items():
# 		exhibition = Exhibition.objects.first()
# 		setattr(exhibition, key, value)
# 		exhibition.save()
'''def list_of_exhibition(request):
	exhibitions = Exhibition.objects.filter(date__gte=timezone.now())
	return render(request, 'index.html', {'exhibitions': exhibitions})'''
class ExhibitionListView(ListView):
	model = Exhibition
	context_object_name = 'exhibitions'
	#template_name = 'index.html'

	def get_queryset(self):
		qs = super(ExhibitionListView, self).get_queryset()
		qs = qs.filter(date__gte=timezone.now())
		return qs
'''def detail(request, pk):
	exhibition = Exhibition.objects.get(id=pk)
	collections = Collection.objects.filter(exhibition__pk=pk)
	sponsors = Sponsor.objects.filter(sponsor_exhibition__pk=pk)
	assistants = Sponsor.objects.filter(assistant_exhibition__pk=pk)
	return render(request, 'exhibition/detail.html', {'exhibition': exhibition, 'collections': collections, 'sponsors': sponsors, 'assistants': assistants})'''
class ExhibitionDetailView(DetailView):
	model = Exhibition
	def get_context_data(self, **kwargs):
		context = super(ExhibitionDetailView, self).get_context_data(**kwargs)
		logger.debug("Exhibitions detail view has been debugged")
		logger.info("Logger of exhibitions detail view informs you!")
		logger.warning("Logger of exhibitions detail view warns you!")
		logger.error("Exhibitions detail view went wrong!")
		context['collections'] = Collection.objects.filter(exhibition__pk=self.object.pk)
		context['sponsors'] = Sponsor.objects.filter(sponsor_exhibition__pk=self.object.pk)
		context['assistants'] = Sponsor.objects.filter(assistant_exhibition__pk=self.object.pk)
		return context

'''def create(request):
	if request.method =='POST':
		form = ExhibitionModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Выставка {} успешно добавлена.'.format(application.name)
			messages.success(request, mes)
			return redirect('index')
	else:
		form = ExhibitionModelForm()
		return render(request, 'exhibition/add.html', {'form':form})'''
class ExhibitionCreateView(CreateView):
	model = Exhibition
	success_url = reverse_lazy('index')

	def get_context_data(self, **kwargs):
		context = super(ExhibitionCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Создание новой выставки'
		return context

	def form_valid(self, form):
		message = super(ExhibitionCreateView, self).form_valid(form)
		mes = u'Выставка {} успешно добавлена.'.format(self.object.name)
		messages.success(self.request, mes)
		return message

'''def edit(request, pk):
	application = Exhibition.objects.get(id=pk)
	if request.method =='POST':
		form = ExhibitionModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			mes = u'Данные изменены.'
			messages.success(request, mes)
	else:
		form = ExhibitionModelForm(instance=application)
	return render(request, 'exhibition/edit.html', {'form':form})'''
class ExhibitionUpdateView(UpdateView):
	model = Exhibition
	def get_success_url(self):
		return reverse_lazy('exhibition:detail', kwargs={'pk':self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(ExhibitionUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Редактирование данных о выставке'
		return context

	def form_valid(self, form):
		message = super(ExhibitionUpdateView, self).form_valid(form)
		mes = u'Данные изменены.'
		messages.success(self.request, mes)
		return message

'''def remove(request, pk):
	application = Exhibition.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Высавка {} была удалена.'.format(application.name)
			messages.success(request, mes)
			return redirect('index')
	return render(request, 'exhibition/remove.html', {'collector':application})'''
class ExhibitionDeleteView(DeleteView):
	model = Exhibition
	success_url = reverse_lazy('index')

	def delete(self, request, *args, **kwargs):
		ret_msg = super(ExhibitionDeleteView, self).delete(request, *args, **kwargs)
		mes = u'Высавка {} была удалена.'.format(self.object.name)
		messages.success(self.request, mes)
		return ret_msg