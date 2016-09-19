# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from collector.models import Collector
from sponsors.models import Sponsor

# Create your models here.
	
class Collection(models.Model):
	name = models.CharField(u'Название коллекции', max_length=55)
	description = models.TextField(u'Описание', null=True, blank=True)
	collector = models.ForeignKey(Collector, verbose_name=u'Коллекционер', null=True, blank=True)

	def __unicode__(self):
		return self.name
	

class Exhibition(models.Model):
	name = models.CharField(u'Назвние выставки', max_length=55)
	date = models.DateTimeField(u'Дата и время проведения')
	short_description = models.CharField(u'Краткое описание', max_length=255)
	description = models.TextField(u'Описание', null=True, blank=True)
	collection = models.ManyToManyField(Collection, verbose_name=u'Коллекции')
	sponsor = models.ForeignKey(Sponsor, verbose_name=u'Спонсор', related_name="sponsor_exhibition", null=True, blank=True)
	assistant = models.ForeignKey(Sponsor, verbose_name=u'Ассистент', related_name="assistant_exhibition", null=True, blank=True)

	def __unicode__(self):
		return self.name

	def collection_name(self):
		return self.collection.name 