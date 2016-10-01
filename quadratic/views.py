# -*- coding: utf-8 -*-
# TODO doc string
# TODO don't keep unnecessary comments
# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from django.views import generic
# from quadratic.forms import QuadraticForm
# from django.contrib import messages
from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    # TODO doc string
    result = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            discr = b * b - 4 * a * c
            # TODO clear to long strings
            if discr < 0:
                message = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
            elif discr == 0:
                x = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
                message = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = {}".format(
                    x)
            else:
                x1 = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
                x2 = round((-b - discr ** (1 / 2.0)) / 2 * a, 1)
                message = "Квадратное уравнение имеет два действительных корня: x1 = {}, x2 = {}".format(
                    x1, x2)

            result['d'] = 'Дискриминант: {}'.format(discr)
            result['message'] = message

    else:
        form = QuadraticForm()
    result['form'] = form
    return render(request, 'quadratic/results.html', result)

# TODO don't keep unnecessary comments
'''def quadratic_results(request, a, b, c):
	form = QuadraticForm()
	#if request.method =='POST':
	#	form = QuadraticForm(request.POST)
	#	if form.is_valid():
	#		form.cleaned_data
	#		coefficient = form.save()
	#		message.success(request,'=)')
	#else:
	#	form = QuadraticForm()
	error_message_a = ''
	error_message_b = ''
	error_message_c = ''
	message_discr = ''
	message = ''
	roots = ''
	error = False
	if not a:
		error_message_a = u'коэффициент не определен'
		error = True
	elif not a.isdigit() and '-' not in a:
		error_message_a = u'коэффициент не целое число'
		error = True
	elif int(a) == 0:
		error_message_a = u'коэффициент при первом слагаемом уравнения не может быть равным нулю'
		error = True
			
	if not b:
		error_message_b = u'коэффициент не определен'
		error = True
	elif not b.isdigit() and '-' not in b:
		error_message_b = u'коэффициент не целое число'
		error = True
	if not c:
		error_message_c = u'коэффициент не определен'
		error = True
	elif not c.isdigit() and '-' not in c:
		error_message_c = u'коэффициент не целое число'
		error = True
	if not error:
		if '-' in a:
			a = -int(a[1:])
		else:
			a = int(a)
		if '-' in b:
			b = -int(b[1:])
		else:
			b = int(b)
		if '-' in c:
			c = -int(c[1:])
		else:
			c = int(c)
		discr = pow(b, 2.0) - 4 * a * c
		message_discr = u'Дискриминант: {}'.format(discr)
		if discr < 0:
			message = u'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			roots = ''
		elif discr == 0:
			x1 = round(float(-b / (2.0*a)),1)
			message = u'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень:'
			roots = 'x = {}'.format(x1)
		elif discr > 0:
			x1 = round(float((-b + (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			x2 = round(float((-b - (b*b - 4*a*c)**(1/2.0)) / (2.0*a)), 1)
			message = u'Квадратное уравнение имеет два действительных корня:'
			roots = 'x1 = {}, x2 = {}'.format(x1, x2)
	return render(request, 'results.html', {'a':a, 'b':b, 'c':c, 'error_message_a':error_message_a, 
											'error_message_b':error_message_b, 'error_message_c':error_message_c, 
											'message_discr':message_discr, 'message':message, 'roots':roots, 'form':form})'''
