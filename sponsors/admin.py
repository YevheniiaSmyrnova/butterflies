# -*- coding: utf-8 -*-
# TODO doc string
from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    # TODO doc string
    fieldsets = [
        (u'Основная информация',
         {'fields': ['user', 'date_of_birth', 'gender']}),
        (u'Контактная информация', {'fields': ['phone', 'address', 'skype']}),
        (u'Описание', {'fields': ['description']}),
    ]
    list_display = ('user_full_name', 'gender', 'skype', 'description')


# TODO don't keep unnecessary comments
# list_filter = ['user_is_staff']


admin.site.register(Sponsor, SponsorAdmin)
