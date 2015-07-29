# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='TourBuilderProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=250)),
                ('main_kind', models.CharField(max_length=20)),
                ('service_kind', models.CharField(max_length=30)),
                ('account', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TouristProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('location', models.CharField(null=True, max_length=250, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('gender', models.BooleanField()),
                ('account', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('register_time', models.DateTimeField(default=datetime.datetime.now)),
                ('picture', models.FileField(upload_to='static/user/img/', null=True, blank=True, default='static/user/img/default.jpg')),
                ('kind', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='touristprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM'),
        ),
        migrations.AddField(
            model_name='tourbuilderprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM'),
        ),
        migrations.AddField(
            model_name='managerprofile',
            name='user',
            field=models.OneToOneField(to='user.UserM'),
        ),
    ]
