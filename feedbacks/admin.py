# -*- coding: utf-8 -*-
# TODO doc string
from django.contrib import admin

from feedbacks.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    # TODO doc string
    fieldsets = [
        (u'Контакты', {'fields': ['name', 'from_email']}),
        (u'Сообщение', {'fields': ['subject', 'message']}),
    ]
    list_display = ('subject', 'name', 'create_date')
    list_filter = ['create_date']
    search_fields = ['name', 'subject']


admin.site.register(Feedback, FeedbackAdmin)
