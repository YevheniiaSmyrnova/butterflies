# -*- coding: utf-8 -*-
"""
Sponsors admin module
"""
from django.contrib import admin

from sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    """
    Sponsor admin
    """
    fieldsets = [
        (u'Основная информация',
         {'fields': ['user', 'date_of_birth', 'gender']}),
        (u'Контактная информация', {'fields': ['phone', 'address', 'skype']}),
        (u'Описание', {'fields': ['description']}),
    ]
    list_display = ('user_full_name', 'gender', 'skype', 'description')


admin.site.register(Sponsor, SponsorAdmin)
