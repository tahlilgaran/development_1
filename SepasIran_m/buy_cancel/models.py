from django.db import models
from define_trip.models import AirplaneSeat,TrainSeat,Table,Room,Tour
from user.models import TouristProfile

STATUS = (
    ('buy' , 'خرید'),
    ('reserve' , 'رزرو'),
    ('cancel' , 'انصراف'),
)
#jadavel gardesh Haye kharidari shode,
class Wanted_Trip(models.Model):
    gardeshgar = models.ForeignKey(TouristProfile)
    status = models.CharField(max_length=20, choices=STATUS) #kharid(bu),rezerve(re),enseraf(ca)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    meli_code = models.CharField(max_length=10)
    peygiry_code = models.CharField(max_length=10)

class Wanted_Tour(models.Model):
    gardesh = models.ForeignKey(Tour)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Hotel(models.Model):
    gardesh = models.ForeignKey(Room )
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Restaurant(models.Model):
    gardesh = models.ForeignKey(Table)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Airplane(models.Model):
    gardesh = models.ForeignKey(AirplaneSeat)
    info = models.OneToOneField(Wanted_Trip)

class Wanted_Train(models.Model):
    gardesh = models.ForeignKey(TrainSeat)
    info = models.OneToOneField(Wanted_Trip)
