# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0007_auto_20150731_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.FileField(default='/static/define_trip/img/default.jpg', upload_to='/static/define_trip/img/'),
        ),
    ]
