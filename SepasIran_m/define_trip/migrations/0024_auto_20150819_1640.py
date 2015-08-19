# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0023_auto_20150808_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bazdid',
            name='tour',
        ),
        migrations.AlterField(
            model_name='airplane',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gardesh',
            name='free',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 40, 37, 683377)),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 40, 37, 683377)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='end_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 40, 37, 680377)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2015, 8, 19, 16, 40, 37, 679377)),
        ),
        migrations.AlterField(
            model_name='train',
            name='capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Bazdid',
        ),
    ]
