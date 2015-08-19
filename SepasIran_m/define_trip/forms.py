from django import forms
from .models import *
from django.forms.extras import SelectDateWidget


class TourForm(forms.ModelForm):
    max_cancel_time = forms.CharField(required=False, label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(required=False, label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required=True, label="*نام تور")
    # other_explain = forms.CharField()
    airplane = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=AirPlaneC)
    train = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=TrainC)
    bus = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=BusC)
    hotel = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=HotelC)
    apartment = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=ApartmentC)
    mosaferkhane = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=Mosaferkhane)
    start = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    end = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    pic1 = forms.FileField(required=True)
    pic2 = forms.FileField(required=False)
    pic3 = forms.FileField(required=False)
    pic4 = forms.FileField(required=False)


    class Meta:
        model = Tour
        fields = ('tour_kind','destination','source','start_t','end_t','capacity','entire_capacity','leader',
                  'leader_c','cost','destination_explain','move_explain')

    def __init__(self , *args , **kwargs):
        super(TourForm, self).__init__(*args, **kwargs)
        self.fields['start_t'].widget = forms.TimeInput(attrs={
            'class': 'form-control','placeholder': 'hh:mm'})
        self.fields['end_t'].widget = forms.TimeInput(attrs={
            'class': 'form-control','placeholder': 'hh:mm'})
        self.fields['start_t'].widget = forms.TimeInput(attrs={
            'class': 'form-control','placeholder': 'hh:mm'})
        self.fields['capacity'].widget = forms.IntegerField(attrs={
            'class': 'form-control'})
        self.fields['entire_capacity'].widget = forms.IntegerField(attrs={
            'class': 'form-control'})
        self.fields['cost'].widget = forms.TimeInput(attrs={
            'class': 'form-control','placeholder': 'تومان'})

class AirPlaneForm(forms.ModelForm):
    max_cancel_time = forms.CharField(required=False,label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(required=False,label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True)
    # other_explain = forms.CharField()
    start = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))

    class Meta:
        model = AirPlane
        fields = ('destination','source','start_t','cost')
    def __init__(self , *args , **kwargs):
        super(AirPlaneForm, self).__init__(*args, **kwargs)
        self.fields['start_t'].widget = forms.TimeInput(attrs={
                'class': 'form-control','placeholder': 'hh:mm'})

class TrainForm(forms.ModelForm):
    max_cancel_time = forms.CharField(required=False,label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(required=False, label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True)
    # other_explain = forms.CharField()
    start = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))

    class Meta:
        model = Train
        fields = ('destination','source','start_t','cost')
    def __init__(self , *args , **kwargs):
        super(TrainForm, self).__init__(*args, **kwargs)
        self.fields['start_t'].widget = forms.TimeInput(attrs={
                'class': 'form-control','placeholder': 'hh:mm'})


class HotelForm(forms.ModelForm):
    max_cancel_time = forms.CharField(required=False,label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(required=False,label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True)
    pic1 = forms.FileField(required=True)
    pic2 = forms.FileField(required=False)
    pic3 = forms.FileField(required=False)
    pic4 = forms.FileField(required=False)

    class Meta:
        model = Hotel
        fields = ('city',)

class HotelRoomForm(forms.Form):

    start = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    end = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))


class RestaurantForm(forms.ModelForm):
    max_cancel_time = forms.CharField(required=False,label="گردشگران تا چند روز قبل از آغاز تور امکان انصراف دارند؟")
    free = forms.CharField(required=False,label="درصد تخفیف برای اعضای سامانه سپاس ایران")
    name = forms.CharField(required= True)
    pic1 = forms.FileField(required=True)
    pic2 = forms.FileField(required=False)
    pic3 = forms.FileField(required=False)
    pic4 = forms.FileField(required=False)

    class Meta:
        model = Restaurant
        fields = ('city',)

class RestaurantRoomForm(forms.Form):

    start = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
    end = forms.DateField(initial=datetime.date.today,widget=SelectDateWidget(attrs={'type':"date" ,'class':'col-md-2 , form-control'}))
