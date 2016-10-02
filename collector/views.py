# -*- coding: utf-8 -*-
'''
Collector views module
'''
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


class CollectorListView(ListView):
    '''
    List of collector
    '''
    model = Collector
    context_object_name = 'collectors'
    paginate_by = 3


class CollectorDetailView(DetailView):
    '''
    Detail about collector
    '''
    model = Collector

    def get_context_data(self, **kwargs):
        '''
        Extends context data
        :param kwargs:
        :return: context
        '''
        context = super(CollectorDetailView, self).get_context_data(**kwargs)
        logger.debug("Collectors detail view has been debugged")
        logger.info("Logger of collectors detail view informs you!")
        logger.warning("Logger of collectors detail view warns you!")
        logger.error("Collectors detail view went wrong!")
        context['collections'] = Collection.objects.filter(
            collector__pk=self.object.pk)
        return context


class CollectorCreateView(CreateView):
    '''
    Add new collector
    '''
    model = Collector
    success_url = reverse_lazy('collector:list')

    def get_context_data(self, **kwargs):
        '''
        Extends context data
        :param kwargs:
        :return: context
        '''
        context = super(CollectorCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание нового коллекционера'
        return context

    def form_valid(self, form):
        '''
        The successful addition of new collector
        :param form:
        :return: message
        '''
        message = super(CollectorCreateView, self).form_valid(form)
        mes = u'Коллекционер {} {} успешно добавлен.'.format(
            self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return message


class CollectorUpdateView(UpdateView):
    '''
    Edit information about collector
    '''
    model = Collector

    def get_success_url(self):
        '''
        Get success url
        :return: get success url
        '''
        return reverse_lazy('collector:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        '''
        Extends context data
        :param kwargs:
        :return: context
        '''
        context = super(CollectorUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных коллекционера'
        return context

    def form_valid(self, form):
        '''
        The successful edition of collector
        :param form:
        :return: message
        '''
        message = super(CollectorUpdateView, self).form_valid(form)
        mes = u'Данные изменены.'
        messages.success(self.request, mes)
        return message


class CollectorDeleteView(DeleteView):
    '''
    Delete information about collector
    '''
    model = Collector
    success_url = reverse_lazy('collector:list')

    def delete(self, request, *args, **kwargs):
        '''
        The successful deletion of collector
        :param request:
        :param args:
        :param kwargs:
        :return: message
        '''
        ret_msg = super(CollectorDeleteView, self).delete(request, *args,
                                                          **kwargs)
        mes = u'Коллекционер {} {} был успешно удален.'.format(
            self.object.name, self.object.surname)
        messages.success(self.request, mes)
        return ret_msg


def add_collection(request, pk):
    '''
    Add new collection
    '''
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
