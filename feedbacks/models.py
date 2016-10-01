# -*- coding: utf-8 -*-
# TODO doc string
from datetime import datetime

from django.db import models


class Feedback(models.Model):
    # TODO doc string
    name = models.CharField(u'Имя отправителя', max_length=55)
    subject = models.CharField(u'Тема сообщения', max_length=55)
    message = models.TextField(u'Текст сообщения')
    from_email = models.EmailField(u'Email отправителя')
    create_date = models.DateField(u'Дата и время создания',
                                   default=datetime.now())

    def __unicode__(self):
        # TODO doc string
        return self.subject
