# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gardesh',
            name='degree',
            field=models.CharField(max_length=2, choices=[('G', 'Freshman'), ('S', 'Sophomore'), ('B', 'Junior')]),
        ),
        migrations.AlterField(
            model_name='gardesh',
            name='kind',
            field=models.CharField(max_length=2, choices=[('T', 'Freshman'), ('TR', 'Sophomore'), ('A', 'Junior'), ('H', 'Senior'), ('R', 'Senior')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='degree',
            field=models.CharField(max_length=2, choices=[('G', 'Freshman'), ('S', 'Sophomore'), ('B', 'Junior')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='kind',
            field=models.CharField(max_length=2, choices=[('H', 'Freshman'), ('A', 'Sophomore'), ('M', 'Junior')]),
        ),
        migrations.AlterField(
            model_name='transferdevice',
            name='degree',
            field=models.CharField(max_length=2, choices=[('G', 'Freshman'), ('S', 'Sophomore'), ('B', 'Junior')]),
        ),
        migrations.AlterField(
            model_name='transferdevice',
            name='kind',
            field=models.CharField(max_length=2, choices=[('A', 'Freshman'), ('T', 'Sophomore'), ('B', 'Junior')]),
        ),
    ]
