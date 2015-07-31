# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0008_auto_20150731_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airplane',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='name',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='train',
            name='name',
        ),
        migrations.AddField(
            model_name='hotel',
            name='other_explain',
            field=models.TextField(null=True, blank=True),
        ),
    ]
