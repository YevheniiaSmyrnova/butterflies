'''
Main views module
'''
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


class IndexView(TemplateView):
    '''
    Main page
    '''
    template_name = 'index.html'


class FactsView(TemplateView):
    '''
    Interesting facts page
    '''
    template_name = 'facts.html'


class PoemsView(TemplateView):
    '''
    Poems page
    '''
    template_name = 'poems.html'


class ContactView(TemplateView):
    '''
    Contact page
    '''
    template_name = 'contact.html'


def custom_page_not_found(request):
    '''
    Page not found
    :param request:
    :return: Page 404
    '''
    response = render_to_response('404.html')
    response.status_code = 404
    return response
