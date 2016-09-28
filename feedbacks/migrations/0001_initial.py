# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55, verbose_name='\u0418\u043c\u044f \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('subject', models.CharField(max_length=55, verbose_name='\u0422\u0435\u043c\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('message', models.TextField(verbose_name='\u0422\u0435\u043a\u0441\u0442 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f')),
                ('from_email', models.EmailField(max_length=75, verbose_name='Email \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f')),
                ('create_date', models.DateField(default=datetime.datetime(2016, 9, 26, 10, 37, 31, 348632), verbose_name='\u0414\u0430\u0442\u0430 \u0438 \u0432\u0440\u0435\u043c\u044f \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
