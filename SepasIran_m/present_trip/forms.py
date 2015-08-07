__author__ = 'farzanehtahooni'
from define_trip.models import CITY
from django import forms

class SearchForm(forms.Form):
    source = forms.ChoiceField(choices=CITY)
    destination = forms.ChoiceField(choices=CITY)





