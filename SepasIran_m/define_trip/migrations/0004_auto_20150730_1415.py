# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0003_auto_20150730_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agreement',
            name='name',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='exclusive_cost',
        ),
        migrations.AlterField(
            model_name='tour',
            name='tour_kind',
            field=models.CharField(choices=[('NAT', 'طبیعت گردی'), ('INTER', 'ایران گردی'), ('OUTER', 'جهان گردی'), ('HOLLY', 'زیارتی')], max_length=30),
        ),
    ]
