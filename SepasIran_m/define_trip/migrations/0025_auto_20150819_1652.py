# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0024_auto_20150819_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 52, 21, 424629)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 52, 21, 424629)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 52, 21, 420629)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 52, 21, 420629)),
        ),
    ]
