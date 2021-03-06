# -*- coding: utf-8 -*-
'''
Feedbacks admin module
'''
from django.contrib import admin

from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    '''
    Feedback admin
    '''
    fieldsets = [
        (u'Контакты', {'fields': ['name', 'from_email']}),
        (u'Сообщение', {'fields': ['subject', 'message']}),
    ]
    list_display = ('subject', 'name', 'create_date')
    list_filter = ['create_date']
    search_fields = ['name', 'subject']


admin.site.register(Feedback, FeedbackAdmin)
