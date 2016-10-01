# -*- coding: utf-8 -*-
# TODO doc string
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    # TODO doc string
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        # TODO doc string
        return self.question_text

    def was_published_recently(self):
        # TODO doc string
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # TODO doc string
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        # TODO doc string
        return self.choice_text
