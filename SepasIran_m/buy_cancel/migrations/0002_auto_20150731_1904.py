# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_cancel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted_hotel',
            name='gardesh',
            field=models.ForeignKey(to='define_trip.Room'),
        ),
        migrations.AlterField(
            model_name='wanted_restaurant',
            name='gardesh',
            field=models.ForeignKey(to='define_trip.Table'),
        ),
    ]
