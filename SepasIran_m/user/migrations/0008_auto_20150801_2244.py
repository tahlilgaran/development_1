# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20150801_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourbuilderprofile',
            name='kind',
            field=models.CharField(max_length=20, choices=[('Tour', 'تور'), ('Train', 'قطار'), ('AirPlane', 'هواپیما'), ('Hotel', 'هتل'), ('Restaurant', 'رستوران')]),
        ),
    ]
