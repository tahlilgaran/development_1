# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150731_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='account',
        ),
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='main_kind',
        ),
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='service_kind',
        ),
        migrations.AddField(
            model_name='tourbuilderprofile',
            name='kind',
            field=models.CharField(default=0, max_length=20, choices=[('T', 'تور'), ('TR', 'قطار'), ('A', 'هواپیما'), ('H', 'هتل'), ('R', 'رستوران')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='touristprofile',
            name='has_payed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='touristprofile',
            name='gender',
            field=models.CharField(max_length=10, choices=[('female', 'زن'), ('male', 'مرد')]),
        ),
    ]
