from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_KIND = (
    ('gardeshgar', 'گردشگر'),
    ('gardeshsaz', 'گردشساز'),
    ('manager' , 'مدیر')
)

KIND = (
    ('Tour', 'تور'),
    ('Train', 'قطار'),
    ('AirPlane', 'هواپیما'),
    ('Hotel', 'هتل'),
    ('Restaurant', 'رستوران'),
)

GENDER = (
    ('female','زن'),
    ('male','مرد'),
)
class UserM(models.Model):
    user = models.OneToOneField(User, related_name='userm')
    register_time = models.DateTimeField(default=datetime.now)
    picture = models.FileField(upload_to="static/user/img/", default="static/user/img/default.jpg" , null=True, blank=True)
    kind = models.CharField(max_length=10, choices=USER_KIND) #? what is this? redundant

    def __str__(self):
        return str(self.user)

class TouristProfile(models.Model):
    user = models.OneToOneField(UserM,related_name='tprofile')
    location = models.CharField(max_length=250, null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    account = models.IntegerField(default=0)
    has_payed = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.user)

    def age(self):
        year = datetime.now().year
        age = year - self.birthday.year
        return age


class TourBuilderProfile(models.Model):
    user = models.OneToOneField(UserM,related_name='bprofile')  # username is sabt number
    kind = models.CharField(max_length= 20 , choices=KIND)

    def __str__(self):
        return "{}".format(self.user)#bug fixed by yeganeh


class ManagerProfile(models.Model):
    user = models.OneToOneField(UserM,related_name='mprofile')
    # maryam poresh kon

    def __str__(self):
        return "{}".format(self.user.username)

