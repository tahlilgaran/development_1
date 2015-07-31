# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0011_auto_20150731_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='kind',
        ),
        migrations.AddField(
            model_name='gardesh',
            name='kind',
            field=models.CharField(max_length=2, choices=[('T', 'تور'), ('TR', 'قطار'), ('A', 'هواپیما'), ('H', 'هتل'), ('R', 'رستوران')], default=0),
            preserve_default=False,
        ),
    ]
