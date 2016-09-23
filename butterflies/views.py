from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic


def contact(request):
	return render(request, 'contact.html')

def news(request):
	return render(request, 'news.html')

def morpho_rhetenor(request):
	return render(request, 'morpho_rhetenor.html')

def custom_page_not_found(request):
	response = render_to_response('404.html')
	response.status_code = 404
	return response
