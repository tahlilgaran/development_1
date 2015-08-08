# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0022_room_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='address',
            field=models.TextField(default=datetime.datetime(2015, 8, 8, 4, 52, 32, 502790, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address',
            field=models.TextField(default=datetime.datetime(2015, 8, 8, 4, 52, 43, 352098, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gardesh',
            name='kind',
            field=models.CharField(max_length=25, choices=[('tour', 'تور'), ('train', 'قطار'), ('airplane', 'هواپیما'), ('hotel', 'هتل'), ('restaurant', 'رستوران')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='kind',
            field=models.CharField(max_length=25, choices=[('H', 'هتل'), ('A', 'هتل آپارتمان'), ('M', 'مسافرخانه'), ('C', 'چادر')]),
        ),
        migrations.AlterField(
            model_name='transferdevice',
            name='kind',
            field=models.CharField(max_length=25, choices=[('A', 'هواپیما'), ('T', 'قطار'), ('B', 'اتوبوس')]),
        ),
    ]
