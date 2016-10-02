# -*- coding: utf-8 -*-
'''
Feedbacks models module
'''
from datetime import datetime

from django.db import models


class Feedback(models.Model):
    '''
    Feedback model
    '''
    name = models.CharField(u'Имя отправителя', max_length=55)
    subject = models.CharField(u'Тема сообщения', max_length=55)
    message = models.TextField(u'Текст сообщения')
    from_email = models.EmailField(u'Email отправителя')
    create_date = models.DateField(u'Дата и время создания',
                                   default=datetime.now())

    def __unicode__(self):
        '''
        Message subject
        :return: message subject
        '''
        return self.subject
