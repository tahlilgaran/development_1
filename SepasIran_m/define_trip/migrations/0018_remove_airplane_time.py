# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0017_remove_bazdid_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airplane',
            name='time',
        ),
    ]
