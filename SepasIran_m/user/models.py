from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

USER_KIND = (
    ('gardeshgar', 'گردشگر'),
    ('gardeshsaz', 'گردشساز'),
    ('manager' , 'مدیر')
)


class UserM(models.Model):
    user = models.OneToOneField(User,related_name='muser')
    register_time = models.DateTimeField(default=datetime.now)
    picture = models.FileField(upload_to="static/user/img/", default="static/user/img/default.jpg" , null=True, blank=True)
    kind = models.CharField(max_length=10, choices=USER_KIND) #? what is this? redundant

    def __str__(self):
        return str(self.user)


class TouristProfile(models.Model):
    user = models.OneToOneField(UserM, related_name='tprofile')
    location = models.CharField(max_length=250, null=True,blank=True)
    birthday = models.DateField(null=True,blank=True)
    gender = models.BooleanField()
    account = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user.user.username)


    def age(self):
        year = datetime.now().year
        age = year - self.birthday.year
        return age


class TourBuilderProfile(models.Model):
    user = models.OneToOneField(UserM, related_name='bprofile')  # username is sabt number
    location = models.CharField(max_length=250)
    main_kind = models.CharField(max_length= 20)   # service or tour be nazaram ina ezafe ast
    service_kind = models.CharField(max_length= 30)  # h / a / r / t be nazarm ina ezafe ast
    account = models.IntegerField(default=0)

    def __str__(self):
        return "{}".format(self.user.user.last_name)



class ManagerProfile(models.Model):
    user = models.OneToOneField(UserM,related_name= 'mprofile')
    # maryam poresh kon

    def __str__(self):
        return "{}".format(self.user.user.username)

