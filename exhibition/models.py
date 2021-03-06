# -*- coding: utf-8 -*-
"""
Exhibiton models module
"""
from django.db import models

from collector.models import Collector
from sponsors.models import Sponsor


class Collection(models.Model):
    """
    Collection model
    """
    name = models.CharField(u'Название коллекции', max_length=55)
    description = models.TextField(u'Описание', null=True, blank=True)
    collector = models.ForeignKey(Collector, verbose_name=u'Коллекционер',
                                  null=True, blank=True)

    def __unicode__(self):
        """
        Collection name
        :return: collection name
        """
        return self.name


class Exhibition(models.Model):
    """
    Exhibition model
    """
    name = models.CharField(u'Название выставки', max_length=55)
    date = models.DateTimeField(u'Дата и время проведения')
    short_description = models.CharField(u'Краткое описание', max_length=255)
    description = models.TextField(u'Описание', null=True, blank=True)
    collection = models.ManyToManyField(Collection, verbose_name=u'Коллекции')
    sponsor = models.ForeignKey(Sponsor, verbose_name=u'Спонсор',
                                related_name="sponsor_exhibition", null=True,
                                blank=True)
    assistant = models.ForeignKey(Sponsor, verbose_name=u'Ассистент',
                                  related_name="assistant_exhibition",
                                  null=True, blank=True)

    def __unicode__(self):
        """
        Exhibition name
        :return: collection name
        """
        return self.name

    def collection_name(self):
        """
        Collection name
        :return: collection name
        """
        return self.collection.name
