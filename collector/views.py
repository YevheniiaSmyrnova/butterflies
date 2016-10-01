# -*- coding: utf-8 -*-
# TODO doc string
import logging

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from collector.forms import CollectionModelForm
from collector.models import Collector
from exhibition.models import Collection

logger = logging.getLogger(__name__)

# TODO clear unnecessary comments
# Create your views here.
'''def list_of_collector(request):
	collectors = Collector.objects.all()
	return render(request, 'collector/list.html', {'collectors': collectors})'''


class CollectorListView(ListView):
    # TODO doc string
    model = Collector
    context_object_name = 'collectors'
    paginate_by = 3

    def get_queryset(self):
        # TODO doc string
        qs = super(CollectorListView, self).get_queryset()
        exhibition_id = self.request.GET.get('exhibition_id', None)
        if exhibition_id:
            qs = qs.filter(exhibition__id=exhibition_id)
        return qs

# TODO clear unnecessary comments
'''def detail(request, pk):
	collector = Collector.objects.get(id=pk)
	collections = Collection.objects.filter(collector__pk=pk)
	return render(request, 'collector/detail.html', {'collector': collector, 'collections':collections})'''


class CollectorDetailView(DetailView):
    # TODO doc string
    model = Collector

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(CollectorDetailView, self).get_context_data(**kwargs)
        logger.debug("Collectors detail view has been debugged")
        logger.info("Logger of collectors detail view informs you!")
        logger.warning("Logger of collectors detail view warns you!")
        logger.error("Collectors detail view went wrong!")
        context['collections'] = Collection.objects.filter(
            collector__pk=self.object.pk)
        return context

# TODO clear unnecessary comments
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
    # TODO doc string
    model = Collector
    success_url = reverse_lazy('collector:list')

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(CollectorCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание нового коллекционера'
        return context

    def form_valid(self, form):
        # TODO doc string
        message = super(CollectorCreateView, self).form_valid(form)
        mes = u'Коллекционер {} {} успешно добавлен.'.format(
            self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return message

# TODO clear unnecessary comments
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
	return render(request, 'collector/detail.html', {'form':form})'''


class CollectorUpdateView(UpdateView):
    # TODO doc string
    model = Collector

    def get_success_url(self):
        # TODO doc string
        return reverse_lazy('collector:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(CollectorUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных коллекционера'
        return context

    def form_valid(self, form):
        # TODO doc string
        message = super(CollectorUpdateView, self).form_valid(form)
        mes = u'Данные изменены.'
        messages.success(self.request, mes)
        return message

# TODO clear unnecessary comments
'''def remove(request, pk):
	application = Collector.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Коллекционер {} {} был удален.'.format(application.surname, application.name)
			messages.success(request, mes)
			return redirect('collector:list')
	return render(request, 'collector/remove.html', {'collector':application})'''


class CollectorDeleteView(DeleteView):
    # TODO doc string
    model = Collector
    success_url = reverse_lazy('collector:list')

    def delete(self, request, *args, **kwargs):
        # TODO doc string
        ret_msg = super(CollectorDeleteView, self).delete(request, *args,
                                                          **kwargs)
        mes = u'Коллекционер {} {} был успешно удален.'.format(
            self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return ret_msg


def add_collection(request, pk):
    # TODO doc string
    collector = Collector.objects.get(id=pk)
    if request.method == 'POST':
        form = CollectionModelForm(request.POST)
        if form.is_valid():
            application = form.save()
            mes = u'Коллекция {} успешно добавлена.'.format(application.name)
            messages.success(request, mes)
            return redirect('collector:list')
    else:
        form = CollectionModelForm(initial={'collector': collector})
        return render(request, 'collector/add_collection.html',
                      {'form': form, 'collector': collector})
