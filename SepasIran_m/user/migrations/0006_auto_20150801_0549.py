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
            name='location',
        ),
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='main_kind',
        ),
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='service_kind',
        ),
        migrations.RemoveField(
            model_name='userm',
            name='name',
        ),
        migrations.AddField(
            model_name='tourbuilderprofile',
            name='kind',
            field=models.CharField(choices=[('T', 'تور'), ('TR', 'قطار'), ('A', 'هواپیما'), ('H', 'هتل'), ('R', 'رستوران')], max_length=20, default=0),
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
            field=models.CharField(choices=[('female', 'زن'), ('male', 'مرد')], max_length=10),
        ),
    ]
