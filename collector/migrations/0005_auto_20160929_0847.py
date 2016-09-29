# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0004_auto_20160929_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='photo',
            field=models.ImageField(upload_to=b'photos/', width_field=200, null=True, verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f', blank=True),
            preserve_default=True,
        ),
    ]
