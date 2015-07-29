# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('percent', models.FloatField()),
                ('kind', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AirPlane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('start_t', models.TimeField()),
                ('time', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AirplaneSeat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('full', models.BooleanField(default=False)),
                ('airplane', models.ForeignKey(related_name='seat', to='define_trip.AirPlane')),
            ],
        ),
        migrations.CreateModel(
            name='Bazdid',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('location_name', models.CharField(max_length=255)),
                ('time', models.DateField()),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Gardesh',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=30)),
                ('final_rank', models.FloatField(null=True, blank=True)),
                ('order_rank', models.FloatField(null=True, blank=True)),
                ('comment_rank', models.FloatField(null=True, blank=True)),
                ('degree', models.CharField(max_length=30)),
                ('max_cancel_time', models.IntegerField(default=2)),
                ('free', models.FloatField(default=1)),
                ('define_time', models.DateTimeField(default=datetime.datetime.now)),
                ('agreement', models.ForeignKey(to='define_trip.Agreement')),
                ('builder', models.ForeignKey(to='user.TourBuilderProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('gardesh', models.ForeignKey(related_name='hotel', to='define_trip.Gardesh')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=1)),
                ('degree', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('pict', models.FileField(upload_to='static/define_trip/img/', default='static/define_trip/img/default.jpg')),
                ('gardesh', models.ForeignKey(to='define_trip.Gardesh')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start_day', models.DateField()),
                ('end_day', models.DateField()),
                ('gardesh', models.ForeignKey(related_name='restaurant', to='define_trip.Gardesh')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('cost_perNight', models.IntegerField()),
                ('hotel', models.ForeignKey(to='define_trip.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomReserve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reserve_start', models.DateField()),
                ('reserve_end', models.DateField()),
                ('room', models.ForeignKey(to='define_trip.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('cost_perClock', models.IntegerField()),
                ('restaurant', models.ForeignKey(to='define_trip.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='TableReserve',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('reserve_date', models.DateField()),
                ('start_reserve', models.TimeField()),
                ('end_reserve', models.TimeField()),
                ('table', models.ForeignKey(to='define_trip.Table')),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('tour_kind', models.CharField(max_length=30)),
                ('start', models.DateField()),
                ('start_t', models.TimeField()),
                ('end', models.DateField()),
                ('end_t', models.TimeField()),
                ('capacity', models.IntegerField()),
                ('has_sold', models.IntegerField(default=0)),
                ('entire_capacity', models.IntegerField()),
                ('leader', models.CharField(max_length=30)),
                ('leader_c', models.CharField(null=True, max_length=50, blank=True)),
                ('exclusive_cost', models.IntegerField()),
                ('entire_cost', models.IntegerField()),
                ('destination_explain', models.TextField(null=True, blank=True)),
                ('move_explain', models.TextField(null=True, blank=True)),
                ('other_explain', models.TextField(null=True, blank=True)),
                ('destination', models.ForeignKey(related_name='tour_dest', to='define_trip.City')),
                ('gardesh', models.ForeignKey(related_name='tour', to='define_trip.Gardesh')),
                ('source', models.ForeignKey(related_name='tour_source', to='define_trip.City')),
                ('stay_location', models.ForeignKey(to='define_trip.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateField()),
                ('start_t', models.TimeField()),
                ('time', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('destination', models.ForeignKey(related_name='train_dest', to='define_trip.City')),
                ('gardesh', models.ForeignKey(related_name='train', to='define_trip.Gardesh')),
                ('source', models.ForeignKey(related_name='train_source', to='define_trip.City')),
            ],
        ),
        migrations.CreateModel(
            name='TrainSeat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
                ('full', models.BooleanField(default=False)),
                ('train', models.ForeignKey(related_name='seat', to='define_trip.Train')),
            ],
        ),
        migrations.CreateModel(
            name='TransferDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('kind', models.CharField(max_length=1)),
                ('degree', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='tour',
            name='transfer_device',
            field=models.ForeignKey(to='define_trip.TransferDevice'),
        ),
        migrations.AddField(
            model_name='bazdid',
            name='tour',
            field=models.ForeignKey(to='define_trip.Tour'),
        ),
        migrations.AddField(
            model_name='airplane',
            name='destination',
            field=models.ForeignKey(related_name='airplain_dest', to='define_trip.City'),
        ),
        migrations.AddField(
            model_name='airplane',
            name='gardesh',
            field=models.ForeignKey(related_name='airplane', to='define_trip.Gardesh'),
        ),
        migrations.AddField(
            model_name='airplane',
            name='source',
            field=models.ForeignKey(related_name='airplain_source', to='define_trip.City'),
        ),
    ]
