# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0018_remove_airplane_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='time',
        ),
    ]
