# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0004_auto_20150730_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='full',
            field=models.BooleanField(default=False),
        ),
    ]
