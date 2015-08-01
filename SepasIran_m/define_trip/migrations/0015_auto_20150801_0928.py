# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0014_gardesh_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='entire_cost',
            new_name='cost',
        ),
        migrations.RemoveField(
            model_name='airplane',
            name='time',
        ),
        migrations.RemoveField(
            model_name='bazdid',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='gardesh',
            name='other_explain',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='name',
        ),
        migrations.RemoveField(
            model_name='train',
            name='time',
        ),
        migrations.AddField(
            model_name='room',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 4, 55, 2, 128651, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 4, 55, 16, 110450, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='start_clock',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='other_explain',
            field=models.TextField(null=True, blank=True),
        ),
    ]
