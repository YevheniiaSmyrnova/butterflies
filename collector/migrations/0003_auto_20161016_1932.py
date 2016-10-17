# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_collector_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'Email'),
        ),
    ]
