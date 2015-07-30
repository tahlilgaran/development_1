# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0002_auto_20150729_0731'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trans_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('amount', models.PositiveIntegerField()),
                ('gardesh', models.ForeignKey(to='define_trip.Gardesh')),
            ],
        ),
        migrations.CreateModel(
            name='Trans_Kind1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('receiver', models.CharField(max_length=10, default='SAMANE')),
                ('info', models.OneToOneField(to='accounting.Trans_info')),
                ('sender', models.ForeignKey(to='user.TouristProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Trans_Kind2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sender', models.CharField(max_length=10, default='SAMANE')),
                ('info', models.OneToOneField(to='accounting.Trans_info')),
                ('receiver', models.ForeignKey(to='user.TourBuilderProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Trans_Kind3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('sender', models.CharField(max_length=10, verbose_name='SAMANE')),
                ('info', models.OneToOneField(to='accounting.Trans_info')),
                ('receiver', models.ForeignKey(to='user.TouristProfile')),
            ],
        ),
    ]
