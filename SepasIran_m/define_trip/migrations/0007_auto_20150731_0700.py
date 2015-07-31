# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0006_auto_20150731_0553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='pict',
            new_name='picture',
        ),
        migrations.RemoveField(
            model_name='airplane',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='train',
            name='picture',
        ),
        migrations.AlterField(
            model_name='airplane',
            name='destination',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='source',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
        migrations.AlterField(
            model_name='tour',
            name='destination',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
        migrations.AlterField(
            model_name='tour',
            name='source',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.CharField(max_length=255, choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')]),
        ),
    ]
