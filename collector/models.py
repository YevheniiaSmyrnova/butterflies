# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Collector(models.Model):
	name = models.CharField(u'Имя', max_length=55)
	surname = models.CharField(u'Фамилия', max_length=55)
	date_of_birth = models.DateField(u'День Рождения')
	photo = models.ImageField(u'Фотография',upload_to='photos/', default='photos/user_photo.jpg')
	email = models.EmailField('Email')
	phone = models.CharField(u'Телефон', max_length=15)
	address = models.CharField(u'Адрес', max_length=55, null=True, blank=True)
	skype = models.CharField('Skype', max_length=55, null=True, blank=True)

	def __unicode__(self):
		return self.name + ' ' + self.surname