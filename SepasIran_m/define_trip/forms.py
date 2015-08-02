from django import forms
from .models import *


class TourForm(forms.ModelForm):
    max_cancel_time = forms.CharField(label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True, label="*نام تور")
    # other_explain = forms.CharField()


    class Meta:
        model = Tour
        fields = ('tour_kind','destination','source','start','start_t','end','end_t','capacity','entire_capacity','leader',
                  'leader_c','cost','destination_explain','move_explain')

    def __init__(self , *args , **kwargs):
        super(TourForm, self).__init__(*args, **kwargs)
        # self.fields['email'].widget = forms.EmailInput(attrs={
        #     'class': 'form-control','placeholder': 'یک ایمیل یکتا و معتبر وارد کنید'})
        # self.fields['firstname'].widget = forms.TextInput(attrs={
        #     'class': 'form-control','placeholder': 'اسم خود را وارد کنید'})
        # self.fields['lastname'].widget = forms.TextInput(attrs={
        #     'class': 'form-control','placeholder': 'نام خانوادگی خود را وارد کنید'})
        # self.fields['username'].widget = forms.TextInput(attrs={
        #     'class': 'form-control','placeholder': 'یک نام کاربری انتخاب کنید'})
        # self.fields['password'].widget = forms.PasswordInput(attrs={
        #     'class': 'form-control','placeholder': 'رمز عبوری حداقل 6 حرفی'})
        # self.fields['confirm_password'].widget = forms.PasswordInput(attrs={
        #     'class': 'form-control','placeholder': 'رمز عبور خود را دوباره وارد نمایید'})
        # self.fields['birthday'].widget = forms.DateInput(attrs={
        #     'class': 'form-control','placeholder': 'yyyy-mm-dd'})
        # self.fields['location'].widget = forms.TextInput(attrs={
        #     'class': 'form-control' ,'label':'شهر','placeholder': 'نام شهر محل سکونت خود را وارد نمایید'})
        # self.fields['gender'].label = "جنسیت*"
        # self.fields['location'].label = "شهر"
        # self.fields['birthday'].label = "تاریخ تولد"
        # self.fields.keyOrder = ['email', 'username','firstname', 'lastname','password','confirm_password','gender', 'birthday', 'location']


class AirPlaneForm(forms.ModelForm):
    max_cancel_time = forms.CharField(label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True, label="*نام تور")
    # other_explain = forms.CharField()

    class Meta:
        model = AirPlane
        fields = ('destination','source','start','start_t','capacity','cost')


class TrainForm(forms.ModelForm):
    max_cancel_time = forms.CharField(label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True, label="*نام تور")
    # other_explain = forms.CharField()

    class Meta:
        model = Train
        fields = ('destination','source','start','start_t','capacity','cost')


class HotelForm(forms.ModelForm):
    max_cancel_time = forms.CharField(label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    # other_explain = forms.CharField()

    class Meta:
        model = Hotel
        fields = ('city','start_day','end_day')


class RestaurantForm(forms.ModelForm):
    max_cancel_time = forms.CharField(label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True, label="*نام تور")
    # other_explain = forms.CharField()

    class Meta:
        model = Restaurant
        fields = ('city','start_day','end_day')
