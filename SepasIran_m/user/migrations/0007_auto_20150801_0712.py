# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20150801_0623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourbuilderprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userm',
            name='name',
        ),
        migrations.AlterField(
            model_name='managerprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM', related_name='mprofile'),
        ),
        migrations.AlterField(
            model_name='tourbuilderprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM', related_name='bprofile'),
        ),
        migrations.AlterField(
            model_name='touristprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM', related_name='tprofile'),
        ),
        migrations.AlterField(
            model_name='userm',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='userm'),
        ),
    ]
