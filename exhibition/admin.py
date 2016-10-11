# -*- coding: utf-8 -*-
"""
Exhibition admin module
"""
from django.contrib import admin

from exhibition.models import Collection, Exhibition


class CollectionAdmin(admin.ModelAdmin):
    """
    Collection admin
    """
    fieldsets = [
        (u'Основная информация', {'fields': ['name', 'collector']}),
        (u'Описание', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'collector')
    list_filter = ['name']
    search_fields = ['name', 'collector']


class ExhibitionAdmin(admin.ModelAdmin):
    """
    Exhibition admin
    """
    fieldsets = [
        (u'Основная информация', {
            'fields': ['name', 'date', 'short_description', 'collection',
                       'sponsor', 'assistant']}),
        (u'Описание', {'fields': ['description'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'date', 'short_description')
    list_filter = ['date']
    search_fields = ['name', 'date']


admin.site.register(Collection, CollectionAdmin)
admin.site.register(Exhibition, ExhibitionAdmin)
