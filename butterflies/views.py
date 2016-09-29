from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView


class NewsView(TemplateView):
	template_name = 'news.html'

class IndexView(TemplateView):
	template_name = 'index.html'

class ContactView(TemplateView):
	template_name = 'contact.html'

def morpho_rhetenor(request):
	return render(request, 'morpho_rhetenor.html')

def custom_page_not_found(request):
	response = render_to_response('404.html')
	response.status_code = 404
	return response
