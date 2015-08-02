from django.contrib.auth.models import User
from django.db import models
from django import forms

# Create your models here.
from django.forms import ModelForm
from define_trip.models import Tour
from user.models import UserM


CHOICES = (('1', 'عالی',), ('2', 'خوب',),('1', 'متوسط',), ('2', 'بد',),('1', 'خیلی بد',))

class OnlineComment(models.Model):
    user = models.OneToOneField(UserM)
    tour = models.OneToOneField(Tour)
    body = models.CharField( max_length= 100)
    date = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.user.username) #todo


class RatingComment(models.Model):
    user = models.OneToOneField(UserM)
    tour = models.OneToOneField(Tour)
    Q1 = models.IntegerField()
    Q2 = models.IntegerField()
    Q3 = models.IntegerField()
    Q4 = models.IntegerField()
    Q5 = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.user.username) #todo


class OnlineCommentForm(ModelForm):
    class Meta:
        model = OnlineComment
        fields = ['body']

class RatingCommentForm(ModelForm):
    Q1_c = forms.ChoiceField(widget= forms.RadioSelect , choices= CHOICES)
    class Meta:
        model = RatingComment
        fields = ['Q1','Q2','Q3','Q4','Q5']


