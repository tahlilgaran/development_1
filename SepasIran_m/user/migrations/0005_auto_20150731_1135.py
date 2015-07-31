# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20150731_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userm',
            name='picture',
            field=models.FileField(upload_to='static/user/img/', null=True, blank=True, default='static/user/img/default.jpg'),
        ),
    ]
