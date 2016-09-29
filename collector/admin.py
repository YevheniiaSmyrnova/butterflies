# -*- coding: utf-8 -*-
from django.contrib import admin
from collector.models import Collector
from exhibition.models import Collection

# Register your models here.

class CollectionInline(admin.TabularInline):
    model = Collection
    extra = 1

class CollectorAdmin(admin.ModelAdmin):
	fieldsets = [
		(u'Основная информация',   {'fields': ['name', 'surname', 'date_of_birth', 'photo']}),
		(u'Контактная информация', {'fields': ['email', 'phone', 'address', 'skype']}),
	]
	inlines = [CollectionInline]
	list_display = ('surname', 'name', 'phone', 'email')
	list_filter = ['surname']
	search_fields = ['name', 'surname']


admin.site.register(Collector, CollectorAdmin)