__author__ = 'yeganeh'
from django import forms


class buyerForm(forms.ModelForm):
    number_of_buyer= forms.IntegerField(required=True)
    first_name = forms.CharField(required=True , max_length=250)
    last_name  = forms.CharField(required=False ,max_length=250)
    melli_number = forms.IntegerField(required=True , max_length=10,min_length=10)

   # class Meta:

def __init__(self, *args, **kwargs):
        super(buyerForm, self).__init__(*args, **kwargs)
