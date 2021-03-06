# -*- coding: utf-8 -*-
"""
Sponsors models module
"""
from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Sponsor(models.Model):
    """
    Sponsor model
    """
    user = models.OneToOneField(User, verbose_name=u'Пользователь')
    date_of_birth = models.DateField(u'День Рождения')
    gender = models.CharField(u'Пол',
                              choices=(('M', u'Мужской'), ('F', u'Женский')),
                              max_length=15)
    phone = models.CharField(u'Телефон', max_length=15)
    address = models.CharField(u'Адрес', max_length=55)
    skype = models.CharField('Skype', max_length=55)
    description = models.TextField(u'Описание')

    def __unicode__(self):
        """
        Sponsor name
        :return: sponsor name
        """
        return self.user.get_username()

    def user_full_name(self):
        """
        Sponsor full name
        :return: sponsor full name
        """
        return self.user.get_full_name()
