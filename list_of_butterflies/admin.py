# TODO doc string
from django.contrib import admin

from list_of_butterflies.models import ListOfButterflies


class ListOfButterfliesAdmin(admin.ModelAdmin):
    # TODO doc string
    list_display = ('name', 'pub_date', 'was_published_recently')
    fieldsets = [('General information', {
        'fields': ['name', 'habitat', 'family', 'subfamily', 'pub_date']}),
                 ('Description', {'fields': ['description']}), ]
    list_filter = ['pub_date']


admin.site.register(ListOfButterflies, ListOfButterfliesAdmin)
