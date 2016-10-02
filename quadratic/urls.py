# -*- coding: utf-8 -*-
'''
Quadratic urls module
'''
from django.conf.urls import patterns, url

from quadratic import views

urlpatterns = patterns(
    '',
    url(r'^results/$', views.quadratic_results, name='quadratic_results'),
)
