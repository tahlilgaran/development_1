# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0022_room_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('body', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('tour', models.OneToOneField(to='define_trip.Tour')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RatingComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('Q1', models.IntegerField()),
                ('Q2', models.IntegerField()),
                ('Q3', models.IntegerField()),
                ('Q4', models.IntegerField()),
                ('Q5', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('tour', models.OneToOneField(to='define_trip.Tour')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
