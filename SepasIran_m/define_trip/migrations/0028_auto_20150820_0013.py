# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0027_auto_20150819_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 20, 0, 13, 34, 721877)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 20, 0, 13, 34, 721877)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 20, 0, 13, 34, 719878)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 20, 0, 13, 34, 719878)),
        ),
    ]
