# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0019_remove_train_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 8, 1, 6, 37, 53, 160409, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
