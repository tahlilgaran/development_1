# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buy_cancel', '0002_auto_20150731_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wanted_airplane',
            name='gardesh',
            field=models.ForeignKey(to='define_trip.AirplaneSeat', related_name='wanted_airplane'),
        ),
        migrations.AlterField(
            model_name='wanted_hotel',
            name='info',
            field=models.OneToOneField(related_name='wanted_hotel', to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AlterField(
            model_name='wanted_restaurant',
            name='info',
            field=models.OneToOneField(related_name='wanted_restaurant', to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AlterField(
            model_name='wanted_tour',
            name='info',
            field=models.OneToOneField(related_name='wanted_tour', to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AlterField(
            model_name='wanted_train',
            name='info',
            field=models.OneToOneField(related_name='wanted_train', to='buy_cancel.Wanted_Trip'),
        ),
        migrations.AlterField(
            model_name='wanted_trip',
            name='status',
            field=models.CharField(max_length=20, choices=[('buy', 'خرید'), ('reserve', 'رزرو'), ('cancel', 'انصراف')]),
        ),
    ]
