# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quality_control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinecomment',
            name='user',
            field=models.OneToOneField(to='user.UserM'),
        ),
        migrations.AlterField(
            model_name='ratingcomment',
            name='user',
            field=models.OneToOneField(to='user.UserM'),
        ),
    ]
