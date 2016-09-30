# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0009_auto_20160930_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='photo',
            field=models.ImageField(default=b'', upload_to=b'media/photos/', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0440\u0430\u0444\u0438\u044f'),
            preserve_default=True,
        ),
    ]
