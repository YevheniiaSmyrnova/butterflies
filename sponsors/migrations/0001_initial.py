# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(verbose_name='\u0414\u0435\u043d\u044c \u0420\u043e\u0436\u0434\u0435\u043d\u0438\u044f')),
                ('gender', models.CharField(max_length=15, verbose_name='\u041f\u043e\u043b', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone', models.CharField(max_length=15, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('address', models.CharField(max_length=55, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('skype', models.CharField(max_length=55, verbose_name=b'Skype')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('user', models.OneToOneField(verbose_name='\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
