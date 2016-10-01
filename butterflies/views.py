# TODO doc string
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


class IndexView(TemplateView):
    # TODO doc string
    template_name = 'index.html'


class FactsView(TemplateView):
    # TODO doc string
    template_name = 'facts.html'


class PoemsView(TemplateView):
    # TODO doc string
    template_name = 'poems.html'


class ContactView(TemplateView):
    # TODO doc string
    template_name = 'contact.html'


def morpho_rhetenor(request):
    # TODO doc string
    return render(request, 'morpho_rhetenor.html')


def custom_page_not_found(request):
    # TODO doc string
    response = render_to_response('404.html')
    response.status_code = 404
    return response
