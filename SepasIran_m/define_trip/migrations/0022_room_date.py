# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0021_table_start_clock'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 6, 39, 24, 70134, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
