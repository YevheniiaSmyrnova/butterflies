# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20160919_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='gender',
            field=models.CharField(max_length=15, verbose_name='\u041f\u043e\u043b', choices=[(b'M', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (b'F', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')]),
            preserve_default=True,
        ),
    ]
