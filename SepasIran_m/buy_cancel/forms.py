__author__ = 'yeganeh'
from django import forms

class numberForm(forms.Form):
    number = forms.IntegerField();

class peopleForm(forms.Form):
    first_name= forms.CharField(max_length=200,label="نام")
    last_name= forms.CharField(max_length=200,label="نام خانوادگی")
    melli_number= forms.IntegerField(label="شماره ی ملی")

class hotelForm(forms.Form):
    num_day=forms.IntegerField()
    start_date=forms.DateInput()
    end_date=forms.DateInput()

class tableForm(forms.Form):
    date=forms.DateInput()
    clock=forms.TimeInput()
