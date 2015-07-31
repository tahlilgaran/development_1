# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0013_auto_20150731_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='gardesh',
            name='name',
            field=models.CharField(max_length=255, default=0),
            preserve_default=False,
        ),
    ]
