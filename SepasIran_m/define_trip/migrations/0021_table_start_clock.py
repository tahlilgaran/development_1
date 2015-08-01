# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0020_table_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='start_clock',
            field=models.TimeField(default=datetime.datetime(2015, 8, 1, 6, 38, 42, 935239, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
