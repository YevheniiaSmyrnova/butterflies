# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibition',
            name='name',
            field=models.CharField(max_length=55, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u044b\u0441\u0442\u0430\u0432\u043a\u0438'),
            preserve_default=True,
        ),
    ]
