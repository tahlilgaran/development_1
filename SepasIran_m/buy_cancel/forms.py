__author__ = 'yeganeh'
from django import forms

class numberForm(forms.Form):
    number = forms.IntegerField(required=True)

class peopleForm(forms.Form):
    first_name= forms.CharField(max_length=200,label="نام",required=True)
    last_name= forms.CharField(max_length=200,label="نام خانوادگی",required=True)
    melli_number= forms.IntegerField(label="شماره ی ملی",required=True)
    def clean_melli_number(self):
         melli_number = self.cleaned_data['melli_number']
         if melli_number<=0:
             raise  forms.validationError("کد ملی نمیتواند منفی باشد")
         if len(melli_number)>10 :
             raise forms.ValidationError("کد ملی باید ۱۰ رقم باشد")
         if len(melli_number)<10 :
             raise forms.ValidationError("کد ملی باید ۱۰ رقم باشد")
         return melli_number


class bankForm(forms.Form):
    bank_name = forms.CharField(max_length=200,required=True)
    account_number= forms.IntegerField(required=True)
    def clean_account_number(self):
         account_number = self.cleaned_data['account_number']
         if len(account_number)<13 :
             raise forms.ValidationError("تعداد ارقام شماره ی حساب نادرست است")
         return account_number
