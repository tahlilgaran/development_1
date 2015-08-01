# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quality_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingComment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Q1', models.IntegerField()),
                ('Q2', models.IntegerField()),
                ('Q3', models.IntegerField()),
                ('Q4', models.IntegerField()),
                ('Q5', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
