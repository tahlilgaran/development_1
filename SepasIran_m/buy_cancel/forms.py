__author__ = 'yeganeh'
from django import forms

class numberForm(forms.Form):
    number = forms.IntegerField()

class peopleForm(forms.Form):
    first_name= forms.CharField(max_length=200,label="نام")
    last_name= forms.CharField(max_length=200,label="نام خانوادگی")
    melli_number= forms.IntegerField(label="شماره ی ملی")

class hotelForm(forms.Form):
    num_day=forms.IntegerField()
    start_date=forms.DateField()
    end_date=forms.DateField()

class tableForm(forms.Form):
    date=forms.DateField()
    clock=forms.DateField()
