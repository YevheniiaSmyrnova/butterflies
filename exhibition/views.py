# -*- coding: utf-8 -*-
"""
Exhibition views module
"""
import logging

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor

logger = logging.getLogger(__name__)


class ExhibitionListView(ListView):
    """
    List of exhibition which will
    """
    model = Exhibition
    context_object_name = 'exhibitions'

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(ExhibitionListView, self).get_context_data(**kwargs)
        context['now'] = 'active'
        context['title'] = 'Расписание выставок.'
        return context

    def get_queryset(self):
        """
        Filter exhibition
        :return: exhibition which will
        """
        qs = super(ExhibitionListView, self).get_queryset()
        qs = qs.filter(date__gte=timezone.now())
        return qs


class ExhibitionPastListView(ListView):
    """
    List of exhibition which was
    """
    model = Exhibition
    context_object_name = 'exhibitions'

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(ExhibitionPastListView, self).get_context_data(
            **kwargs)
        context['past'] = 'active'
        context['title'] = 'Выставки, которые прошли.'
        return context

    def get_queryset(self):
        """
        Filter exhibition
        :return: exhibition which was
        """
        qs = super(ExhibitionPastListView, self).get_queryset()
        qs = qs.filter(date__lt=timezone.now())
        return qs


class ExhibitionDetailView(DetailView):
    """
    Detail about exhibition
    """
    model = Exhibition

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(ExhibitionDetailView, self).get_context_data(**kwargs)
        logger.debug("Exhibitions detail view has been debugged")
        logger.info("Logger of exhibitions detail view informs you!")
        logger.warning("Logger of exhibitions detail view warns you!")
        logger.error("Exhibitions detail view went wrong!")
        context['collections'] = Collection.objects.filter(
            exhibition__pk=self.object.pk)
        context['sponsors'] = Sponsor.objects.filter(
            sponsor_exhibition__pk=self.object.pk)
        context['assistants'] = Sponsor.objects.filter(
            assistant_exhibition__pk=self.object.pk)
        return context


class ExhibitionCreateView(CreateView):
    """
    Add new exhibition
    """
    model = Exhibition
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(ExhibitionCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание новой выставки'
        return context

    def form_valid(self, form):
        """
        The successful addition of new exhibition
        :param form:
        :return: message
        """
        message = super(ExhibitionCreateView, self).form_valid(form)
        mes = u'Выставка {} успешно добавлена.'.format(self.object.name)
        messages.success(self.request, mes)
        return message


class ExhibitionUpdateView(UpdateView):
    """
    Edit information about exhibition
    """
    model = Exhibition

    def get_success_url(self):
        """
        Get success url
        :return: get success url
        """
        return reverse_lazy('exhibition:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        """
        Extends context data
        :param kwargs:
        :return: context
        """
        context = super(ExhibitionUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных о выставке'
        return context

    def form_valid(self, form):
        """
        The successful edition of exhibition
        :param form:
        :return: message
        """
        message = super(ExhibitionUpdateView, self).form_valid(form)
        mes = u'Данные изменены.'
        messages.success(self.request, mes)
        return message


class ExhibitionDeleteView(DeleteView):
    """
    Delete information about exhibition
    """
    model = Exhibition
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        """
        The successful deletion of exhibition
        :param request:
        :param args:
        :param kwargs:
        :return: message
        """
        ret_msg = super(ExhibitionDeleteView, self).delete(request, *args,
                                                           **kwargs)
        mes = u'Высавка {} была удалена.'.format(self.object.name)
        messages.success(self.request, mes)
        return ret_msg
