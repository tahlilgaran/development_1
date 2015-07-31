# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0010_auto_20150731_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='other_explain',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='other_explain',
        ),
        migrations.AddField(
            model_name='gardesh',
            name='other_explain',
            field=models.TextField(null=True, blank=True),
        ),
    ]
