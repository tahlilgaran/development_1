# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0014_gardesh_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='name',
        ),
    ]
