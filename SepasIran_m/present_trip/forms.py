import datetime
from django.forms.extras import SelectDateWidget

__author__ = 'farzanehtahooni'
from define_trip.models import CITY,KIND
from django import forms


class SearchForm(forms.Form):
    source = forms.ChoiceField(label='شهری که در آن هستید.',widget=forms.Select(attrs={'class': 'form-control , col-md-6'}),choices=CITY)
    destination = forms.ChoiceField(label='شهری که قصد گردش در آن دارید.',widget=forms.Select(attrs={'class': 'form-control , col-md-6'}),choices=CITY)
    start = forms.DateField(label='از',initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    end = forms.DateField(label='تا',initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    kind = forms.MultipleChoiceField(label='نوع',required=True,widget=forms.CheckboxSelectMultiple(attrs={'class':'salam'}),choices=KIND)


    def __init__(self , *args,**kwargs):
        super(SearchForm,self).__init__(*args,**kwargs)





