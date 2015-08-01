# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0015_remove_tour_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='entire_cost',
            new_name='cost',
        ),
    ]
