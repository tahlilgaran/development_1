# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20150808_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristprofile',
            name='has_payed',
            field=models.BooleanField(default=False),
        ),
    ]
