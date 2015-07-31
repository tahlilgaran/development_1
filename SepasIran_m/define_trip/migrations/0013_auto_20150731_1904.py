# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_cancel', '0002_auto_20150731_1904'),
        ('define_trip', '0012_auto_20150731_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomreserve',
            name='room',
        ),
        migrations.RemoveField(
            model_name='tablereserve',
            name='table',
        ),
        migrations.AddField(
            model_name='table',
            name='full',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='RoomReserve',
        ),
        migrations.DeleteModel(
            name='TableReserve',
        ),
    ]
