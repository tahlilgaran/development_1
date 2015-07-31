# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150731_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userm',
            name='picture',
            field=models.FileField(default='/static/user/img/default.jpg', upload_to='/static/user/img/', blank=True, null=True),
        ),
    ]
