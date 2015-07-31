# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userm',
            name='kind',
            field=models.CharField(choices=[('gardeshgar', 'گردشگر'), ('gardeshsaz', 'گردشساز'), ('manager', 'مدیر')], max_length=10),
        ),
    ]
