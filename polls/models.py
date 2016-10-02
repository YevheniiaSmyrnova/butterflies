# -*- coding: utf-8 -*-
'''
Polls models module
'''
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    '''
    Question model
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        '''
        Question text
        :return: question text
        '''
        return self.question_text

    def was_published_recently(self):
        '''
        Question which was published recently
        :return:
        '''
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    '''
    Answer model
    '''
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        '''
        Answer text
        :return: answer text
        '''
        return self.choice_text
