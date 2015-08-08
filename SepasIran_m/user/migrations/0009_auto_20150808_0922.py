# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20150801_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristprofile',
            name='has_payed',
            field=models.BooleanField(default=True),
        ),
    ]
