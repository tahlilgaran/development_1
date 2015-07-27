# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('define_trip', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wanted_Airplane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gardesh', models.ForeignKey(to='define_trip.AirplaneSeat')),
            ],
        ),
        migrations.CreateModel(
            name='Wanted_Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gardesh', models.ForeignKey(to='define_trip.RoomReserve')),
            ],
        ),
        migrations.CreateModel(
            name='Wanted_Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gardesh', models.ForeignKey(to='define_trip.TableReserve')),
            ],
        ),
        migrations.CreateModel(
            name='Wanted_Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gardesh', models.ForeignKey(to='define_trip.Tour')),
            ],
        ),
        migrations.CreateModel(
            name='Wanted_Train',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('gardesh', models.ForeignKey(to='define_trip.TrainSeat')),
            ],
        ),
        migrations.CreateModel(
            name='Wanted_Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=2)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('meli_code', models.CharField(max_length=10)),
                ('peygiry_code', models.CharField(max_length=10)),
                ('gardeshgar', models.ForeignKey(to='user.TouristProfile')),
            ],
        ),
        migrations.AddField(
            model_name='wanted_train',
            name='info',
            field=models.OneToOneField(to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AddField(
            model_name='wanted_tour',
            name='info',
            field=models.OneToOneField(to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AddField(
            model_name='wanted_restaurant',
            name='info',
            field=models.OneToOneField(to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AddField(
            model_name='wanted_hotel',
            name='info',
            field=models.OneToOneField(to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AddField(
            model_name='wanted_airplane',
            name='info',
            field=models.OneToOneField(to='buy_cancel.Wanted_Trip'),
        ),
    ]
