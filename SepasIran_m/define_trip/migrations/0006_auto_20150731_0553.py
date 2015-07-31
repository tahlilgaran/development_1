# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0005_room_full'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplane',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/airplane/img/', default='static/define_trip/img/default.jpg'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/hotel/img/', default='static/define_trip/img/default.jpg'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/restaurant/img/', default='static/define_trip/img/default.jpg'),
        ),
        migrations.AddField(
            model_name='tour',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/tour/img/', default='static/define_trip/img/default.jpg'),
        ),
        migrations.AddField(
            model_name='train',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/train/img/', default='static/define_trip/img/default.jpg'),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='destination',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='source',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='tour',
            name='destination',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='tour',
            name='source',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='train',
            name='destination',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
        migrations.AlterField(
            model_name='train',
            name='source',
            field=models.CharField(choices=[('تهران', 'تهران'), ('مشهد', 'مشهد'), ('کیش', 'کیش'), ('سمنان', 'سمنان')], max_length=255),
        ),
    ]
