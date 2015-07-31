from django.db import models
from define_trip.models import Gardesh
from user.models import TouristProfile,TourBuilderProfile
# anvaE tarakonesh HA :
# gardeshgar --> samane
# samane --> gardeshsaz
# samane --> gardeshgar

class Trans_info(models.Model):
    date = models.DateField()
    amount = models.PositiveIntegerField()
    gardesh = models.ForeignKey(Gardesh)

class Trans_Kind1(models.Model):#tourist be ma
    info = models.OneToOneField(Trans_info)
    sender = models.ForeignKey(TouristProfile)
    receiver = models.CharField(default='SAMANE' ,max_length=10) # in nabayed taghir kone

class Trans_Kind2(models.Model):# ma be builder
    info = models.OneToOneField(Trans_info)
    sender = models.CharField(default='SAMANE',max_length=10) #in nabayed taghir kone
    receiver = models.ForeignKey(TourBuilderProfile)

class Trans_Kind3(models.Model):# ma be tourist
    info = models.OneToOneField(Trans_info)
    sender = models.CharField('SAMANE',max_length=10)
    receiver = models.ForeignKey(TouristProfile)
