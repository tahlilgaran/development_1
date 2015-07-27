from django.db import models
from define_trip.models import AirplaneSeat,TrainSeat,TableReserve,RoomReserve,Tour
from user.models import TouristProfile

#jadavel gardesh Haye kharidari shode,
class Wanted_Trip(models.Model):
    gardeshgar = models.ForeignKey(TouristProfile)
    status = models.CharField(max_length=2) #kharid(bu),rezerve(re),enseraf(ca)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    meli_code = models.CharField(max_length=10)
    peygiry_code = models.CharField(max_length=10)

class Wanted_Tour(models.Model):
    gardesh = models.ForeignKey(Tour)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Hotel(models.Model):
    gardesh = models.ForeignKey(RoomReserve)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Restaurant(models.Model):
    gardesh = models.ForeignKey(TableReserve)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Airplane(models.Model):
    gardesh = models.ForeignKey(AirplaneSeat)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Train(models.Model):
    gardesh = models.ForeignKey(TrainSeat)
    info = models.OneToOneField(Wanted_Trip)
