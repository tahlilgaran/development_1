# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0016_auto_20150801_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bazdid',
            name='cost',
        ),
    ]
