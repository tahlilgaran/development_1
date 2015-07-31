# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0009_auto_20150731_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(choices=[('Tehran', 'تهران'), ('Mashad', 'مشهد'), ('Kish', 'کیش'), ('Semnan', 'سمنان')], default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(upload_to='static/define_trip/img/'),
        ),
    ]
