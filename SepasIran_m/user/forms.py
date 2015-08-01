from django import forms
from .models import TouristProfile,TourBuilderProfile,UserM
from django.contrib.auth.models import User


class TouristSignUpForm(forms.ModelForm):
    firstname = forms.CharField(label="نام")
    lastname = forms.CharField(label="نام خانوادگی")
    email = forms.EmailField(required=True,label="ایمیل*")
    username = forms.CharField(required=True,label="نام کاربری*")
    password = forms.CharField(required=True,label="رمز عبور*")
    confirm_password = forms.CharField(required=True,label="تکرار رمز عبور*")

    class Meta:
        model = TouristProfile
        fields = ('gender','birthday','location',)

    def __init__(self , *args , **kwargs):
        super(TouristSignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control','placeholder': 'یک ایمیل یکتا و معتبر وارد کنید'})
        self.fields['firstname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'اسم خود را وارد کنید'})
        self.fields['lastname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'نام خانوادگی خود را وارد کنید'})
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'یک نام کاربری انتخاب کنید'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبوری حداقل 6 حرفی'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبور خود را دوباره وارد نمایید'})
        self.fields['birthday'].widget = forms.DateInput(attrs={
            'class': 'form-control','placeholder': 'yyyy-mm-dd'})
        self.fields['location'].widget = forms.TextInput(attrs={
            'class': 'form-control' ,'label':'شهر','placeholder': 'نام شهر محل سکونت خود را وارد نمایید'})
        self.fields['gender'].label = "جنسیت*"
        self.fields['location'].label = "شهر"
        self.fields['birthday'].label = "تاریخ تولد"
        self.fields.keyOrder = ['email', 'username','firstname', 'lastname','password','confirm_password','gender', 'birthday', 'location']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("this username has assigned before")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("your password's length must be more than 6 character")
        return password

    def clean_confirm_password(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError(" the passwords doesn't match")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(password=self.cleaned_data['password'], username=self.cleaned_data['username']
                                        ,email=self.cleaned_data['email'])
        muser = UserM()
        muser.user = user
        if self.cleaned_data['firstname']:
            muser.user.first_name = self.cleaned_data['firstname']
        if self.cleaned_data['lastname']:
            muser.user.last_name = self.cleaned_data['lastname']
        muser.user.save()
        muser.kind = 'gardeshgar'
        muser.save()
        profile = super(TouristSignUpForm,self).save(commit=False)
        profile.user = muser
        if self.cleaned_data['birthday']:
            profile.birthday = self.cleaned_data['birthday']
        if self.cleaned_data['location']:
            profile.location = self.cleaned_data['location']
        profile.gender = self.cleaned_data['gender']
        profile.save()
