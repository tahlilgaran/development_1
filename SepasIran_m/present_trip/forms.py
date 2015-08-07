import datetime
from django.forms.extras import SelectDateWidget

__author__ = 'farzanehtahooni'
from define_trip.models import CITY,KIND
from django import forms


class SearchForm(forms.Form):
    source = forms.ChoiceField(label='شهری که در آن هستید.',choices=CITY)
    destination = forms.ChoiceField(label='شهری که در آن قصد گردش دارید.',choices=CITY)
    start = forms.DateField(label='از',initial=datetime.date.today,widget=SelectDateWidget())
    end = forms.DateField(label='تا',initial=datetime.date.today,widget=SelectDateWidget())
    kind = forms.MultipleChoiceField(label='نوع',required=True,widget=forms.CheckboxSelectMultiple,choices=KIND)




