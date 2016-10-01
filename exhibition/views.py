# -*- coding: utf-8 -*-
# TODO doc string
import logging

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from exhibition.models import Exhibition, Collection
from sponsors.models import Sponsor

logger = logging.getLogger(__name__)

# TODO clear unnecessary comments
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
    # TODO doc string
    model = Exhibition
    context_object_name = 'exhibitions'

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(ExhibitionListView, self).get_context_data(**kwargs)
        context['now'] = 'active'
        context['title'] = 'Расписание выставок.'
        return context

    def get_queryset(self):
        # TODO doc string
        qs = super(ExhibitionListView, self).get_queryset()
        qs = qs.filter(date__gte=timezone.now())
        return qs


class ExhibitionPastListView(ListView):
    # TODO doc string
    model = Exhibition
    context_object_name = 'exhibitions'

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(ExhibitionPastListView, self).get_context_data(
            **kwargs)
        context['past'] = 'active'
        context['title'] = 'Выставки, которые прошли.'
        return context

    def get_queryset(self):
        # TODO doc string
        qs = super(ExhibitionPastListView, self).get_queryset()
        qs = qs.filter(date__lt=timezone.now())
        return qs


'''def detail(request, pk):
	exhibition = Exhibition.objects.get(id=pk)
	collections = Collection.objects.filter(exhibition__pk=pk)
	sponsors = Sponsor.objects.filter(sponsor_exhibition__pk=pk)
	assistants = Sponsor.objects.filter(assistant_exhibition__pk=pk)
	return render(request, 'exhibition/detail.html', {'exhibition': exhibition, 'collections': collections, 'sponsors': sponsors, 'assistants': assistants})'''


class ExhibitionDetailView(DetailView):
    # TODO doc string
    model = Exhibition

    def get_context_data(self, **kwargs):
        # TODO doc string
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

# TODO clear unnecessary comments
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
    # TODO doc string
    model = Exhibition
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(ExhibitionCreateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Создание новой выставки'
        return context

    def form_valid(self, form):
        # TODO doc string
        message = super(ExhibitionCreateView, self).form_valid(form)
        mes = u'Выставка {} успешно добавлена.'.format(self.object.name)
        messages.success(self.request, mes)
        return message


# TODO clear unnecessary comments

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
    # TODO doc string
    model = Exhibition

    def get_success_url(self):
        # TODO doc string
        return reverse_lazy('exhibition:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        # TODO doc string
        context = super(ExhibitionUpdateView, self).get_context_data(**kwargs)
        context['page_title'] = u'Редактирование данных о выставке'
        return context

    def form_valid(self, form):
        # TODO doc string
        message = super(ExhibitionUpdateView, self).form_valid(form)
        mes = u'Данные изменены.'
        messages.success(self.request, mes)
        return message


# TODO clear unnecessary comments

'''def remove(request, pk):
	application = Exhibition.objects.get(id=pk)
	if request.method =='POST':
			application.delete()
			mes = u'Высавка {} была удалена.'.format(application.name)
			messages.success(request, mes)
			return redirect('index')
	return render(request, 'exhibition/remove.html', {'collector':application})'''


class ExhibitionDeleteView(DeleteView):
    # TODO doc string
    model = Exhibition
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        # TODO doc string
        ret_msg = super(ExhibitionDeleteView, self).delete(request, *args,
                                                           **kwargs)
        mes = u'Высавка {} была удалена.'.format(self.object.name)
        messages.success(self.request, mes)
        return ret_msg
