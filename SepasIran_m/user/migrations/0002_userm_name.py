# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userm',
            name='name',
            field=models.CharField(max_length=255, default=0),
            preserve_default=False,
        ),
    ]
