# -*- coding: utf-8 -*-
'''
Quadratic views module
'''
from django.shortcuts import render

from quadratic.forms import QuadraticForm


def quadratic_results(request):
    '''
    solution of the quadratic equation
    :param request: regular http(s) request
    :return: root quadratic equation
    '''
    result = {}
    if request.GET:
        form = QuadraticForm(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            discr = b * b - 4 * a * c
            if discr < 0:
                message = "Дискриминант меньше нуля, квадратное уравнение " \
                          "не имеет действительных решений."
            elif discr == 0:
                x = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
                message = "Дискриминант равен нулю, квадратное уравнение " \
                          "имеет один действительный корень: " \
                          "x1 = x2 = {}".format(x)
            else:
                x1 = round((-b + discr ** (1 / 2.0)) / 2 * a, 1)
                x2 = round((-b - discr ** (1 / 2.0)) / 2 * a, 1)
                message = "Квадратное уравнение имеет два действительных " \
                          "корня: x1 = {}, x2 = {}".format(x1, x2)

            result['d'] = 'Дискриминант: {}'.format(discr)
            result['message'] = message

    else:
        form = QuadraticForm()
    result['form'] = form
    return render(request, 'quadratic/results.html', result)
