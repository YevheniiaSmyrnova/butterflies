# -*- coding: utf-8 -*-
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Sponsor(models.Model):
	user = models.OneToOneField(User, verbose_name=u'Пользователь')
	date_of_birth = models.DateField(u'День Рождения')
	gender = models.CharField(u'Пол', choices=(('M',u'Мужской'), ('F',u'Женский')), max_length=15)
	phone = models.CharField(u'Телефон', max_length=15)
	address = models.CharField(u'Адрес', max_length=55)
	skype = models.CharField('Skype', max_length=55)
	description = models.TextField(u'Описание')
	
	def __unicode__(self):
		return self.user.get_username()

	def user_full_name(self):
		return self.user.get_full_name()

	#def user_is_staff(self):
		#return self.user.is_staff
