# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_collector_poto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collector',
            old_name='poto',
            new_name='photo',
        ),
    ]
