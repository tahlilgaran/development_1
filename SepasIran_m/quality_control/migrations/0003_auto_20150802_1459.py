# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0002_auto_20150802_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecomment',
            name='tour',
            field=models.ForeignKey(to='define_trip.Tour'),
        ),
    ]
