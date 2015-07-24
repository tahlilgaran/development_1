from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class TouristProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=250, null=True,blank=True)
    picture = models.FileField(upload_to="static/users/img/", default="static/users/img/default.jpg" , null=True, blank=True)
    birthday = models.DateField()
    gender = models.BooleanField()

    def __str__(self):
        return "{}".format(self.user.username)

    def age(self):
        year = datetime.now().year
        age = year - self.birthday.year
        return age


class TourBuilderProfile(models.Model):
    user = models.OneToOneField(User)
    location = models.CharField(max_length=250, null=True,blank=True)
    picture = models.FileField(upload_to="static/users/img/", default="static/users/img/default.jpg" , null=True, blank=True)
    kind = models.CharField()   #service or tour

    def __str__(self):
        return "{}".format(self.user.last_name)


class ManagerProfile(models.Model):
    user = models.OneToOneField(User)
    #maryam poresh kon

    def __str__(self):
        return "{}".format(self.user.username)
