# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0003_auto_20150802_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecomment',
            name='user',
            field=models.ForeignKey(to='user.UserM'),
        ),
        migrations.AlterField(
            model_name='ratingcomment',
            name='tour',
            field=models.ForeignKey(to='define_trip.Tour'),
        ),
        migrations.AlterField(
            model_name='ratingcomment',
            name='user',
            field=models.ForeignKey(to='user.UserM'),
        ),
    ]
