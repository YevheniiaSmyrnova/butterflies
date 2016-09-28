# -*- coding: utf-8 -*-
#from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from collector.models import Collector
from exhibition.models import Collection
from collector.forms import CollectorModelForm, CollectionModelForm


# Create your views here.
'''def list_of_collector(request):
	collectors = Collector.objects.all()
	return render(request, 'collector/list.html', {'collectors': collectors})'''
class CollectorListView(ListView):
	model = Collector
	context_object_name = 'collectors'

	def get_queryset(self):
		qs = super(CollectorListView, self).get_queryset()
		exhibition_id = self.request.GET.get('exhibition_id', None)
		if exhibition_id:
			qs = qs.filter(exhibition__id=exhibition_id)
		return qs

'''def detail(request, pk):
	collector = Collector.objects.get(id=pk)
	collections = Collection.objects.filter(collector__pk=pk)
	return render(request, 'collector/detail.html', {'collector': collector, 'collections':collections})'''
class CollectorDetailView(DetailView):
	model = Collector

	def get_context_data(self, **kwargs):
		context = super(CollectorDetailView, self).get_context_data(**kwargs)
		context['collections'] = Collection.objects.filter(collector__pk=self.object.pk)
		return context

'''def create(request):
	if request.method =='POST':
		form = CollectorModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Коллекционер {} {} успешно добавлен.'.format(application.surname, application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	else:
		form = CollectorModelForm()
		return render(request, 'collector/add.html', {'form':form})'''
class CollectorCreateView(CreateView):
	model = Collector
	success_url = reverse_lazy('collector:list')

	def get_context_data(self, **kwargs):
		context = super(CollectorCreateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Создание нового коллекционера'
		return context

	def form_valid(self, form):
		message = super(CollectorCreateView, self).form_valid(form)
		mes = u'Коллекционер {} {} успешно добавлен.'.format(self.object.name, self.object.surname)
		messages.success(self.request, mes)
		return message


'''def edit(request, pk):
	application = Collector.objects.get(id=pk)
	if request.method =='POST':
		form = CollectorModelForm(request.POST, instance=application)
		if form.is_valid():
			application = form.save()
			mes = u'Данные изменены.'
			messages.success(request, mes)
	else:
		form = CollectorModelForm(instance=application)
	return render(request, 'collector/edit.html', {'form':form})'''
class CollectorUpdateView(UpdateView):
	model = Collector
	def get_success_url(self):
		return reverse_lazy('collector:edit', kwargs={'pk':self.object.pk})

	def get_context_data(self, **kwargs):
		context = super(CollectorUpdateView, self).get_context_data(**kwargs)
		context['page_title'] = u'Редоктирование данных коллекционера'
		return context

	def form_valid(self, form):
		message = super(CollectorUpdateView, self).form_valid(form)
		mes = u'Данные изменены.'
		messages.success(self.request, mes)
		return message

'''def remove(request, pk):
	application = Collector.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Коллекционер {} {} был удален.'.format(application.surname, application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	return render(request, 'collector/remove.html', {'collector':application})'''
class CollectorDeleteView(DeleteView):
	model = Collector
	success_url = reverse_lazy('collector:list')

	def delete(self, request, *args, **kwargs):
		ret_msg = super(CollectorDeleteView, self).delete(request, *args, **kwargs)
		mes = u'Коллекционер {} {} был успешно удален.'.format(self.object.name, self.object.surname)
		messages.success(self.request, mes)
		return ret_msg

def add_collection(request, pk):
	collector = Collector.objects.get(id=pk)
	if request.method =='POST':
		form = CollectionModelForm(request.POST)
		if form.is_valid():
			application = form.save()
			mes = u'Коллекция {} успешно добавлена.'.format(application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	else:
		form = CollectionModelForm(initial={'collector': collector})
		return render(request, 'collector/add_collection.html', {'form':form, 'collector': collector})