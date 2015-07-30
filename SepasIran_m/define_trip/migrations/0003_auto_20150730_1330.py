# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0002_auto_20150729_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airplaneseat',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='gardesh',
            name='kind',
        ),
        migrations.AddField(
            model_name='airplane',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tour',
            name='kind',
            field=models.CharField(choices=[('T', 'تور'), ('TR', 'قطار'), ('A', 'هواپیما'), ('H', 'هتل'), ('R', 'رستوران')], max_length=2, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='airplane',
            name='destination',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='source',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='gardesh',
            name='degree',
            field=models.CharField(choices=[('G', 'طلایی'), ('S', 'نقره ای'), ('B', 'برنز')], max_length=2),
        ),
        migrations.AlterField(
            model_name='location',
            name='degree',
            field=models.CharField(choices=[('G', 'طلایی'), ('S', 'نقره ای'), ('B', 'برنز')], max_length=2),
        ),
        migrations.AlterField(
            model_name='location',
            name='kind',
            field=models.CharField(choices=[('H', 'هتل'), ('A', 'هتل آپارتمان'), ('M', 'مسافرخانه'), ('C', 'چادر')], max_length=2),
        ),
        migrations.AlterField(
            model_name='tour',
            name='destination',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='tour',
            name='source',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='transferdevice',
            name='degree',
            field=models.CharField(choices=[('G', 'طلایی'), ('S', 'نقره ای'), ('B', 'برنز')], max_length=2),
        ),
        migrations.AlterField(
            model_name='transferdevice',
            name='kind',
            field=models.CharField(choices=[('A', 'هواپیما'), ('T', 'قطار'), ('B', 'اتوبوس')], max_length=2),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
