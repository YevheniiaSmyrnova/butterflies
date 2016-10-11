# -*- coding: utf-8 -*-
"""
Collector admin module
"""
from django.contrib import admin

from collector.models import Collector
from exhibition.models import Collection


class CollectionInline(admin.TabularInline):
    """
    Collection with have collector
    """
    model = Collection
    extra = 1


class CollectorAdmin(admin.ModelAdmin):
    """
    Collector admin
    """
    fieldsets = [
        (u'Основная информация',
         {'fields': ['name', 'surname', 'date_of_birth', 'photo']}),
        (u'Контактная информация',
         {'fields': ['email', 'phone', 'address', 'skype']}),
    ]
    inlines = [CollectionInline]
    list_display = ('surname', 'name', 'phone', 'email')
    list_filter = ['surname']
    search_fields = ['name', 'surname']


admin.site.register(Collector, CollectorAdmin)
