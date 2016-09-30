from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView


class IndexView(TemplateView):
	template_name = 'index.html'
	
class FactsView(TemplateView):
	template_name = 'facts.html'

class PoemsView(TemplateView):
	template_name = 'poems.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

def morpho_rhetenor(request):
	return render(request, 'morpho_rhetenor.html')

def custom_page_not_found(request):
	response = render_to_response('404.html')
	response.status_code = 404
	return response
