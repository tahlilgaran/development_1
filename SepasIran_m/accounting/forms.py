__author__ = 'yeganeh'
from django import forms
#KIND = (
 #   ('صادرات', 'صادرات'),
 #   ('تجارت', 'تجارت'),
 #   ('کشاورزی', 'کشاورزی'),
 #   ('ملی', 'ملی'),
 #   ('پاسارگاد', 'پاسارگاد'),
 #   ('پارسیان', 'پارسیان'),
 #   ('ملت', 'ملت'),
#)

class bankForm(forms.Form):
    bank_name = forms.CharField(max_length=30,required=True)
    account_number= forms.IntegerField(required=True)

    def clean_account_number(self):
         account_number = self.cleaned_data['account_number']
         if len(account_number)<13 :
             raise forms.ValidationError("تعداد ارقام شماره ی حساب نادرست است")
         return account_number

