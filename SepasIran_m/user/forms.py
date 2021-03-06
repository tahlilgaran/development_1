from django import forms
from .models import *
from django.contrib.auth.models import User


class TouristSignUpForm(forms.ModelForm):
    firstname = forms.CharField(required=False,label="نام")
    lastname = forms.CharField(required=False,label="نام خانوادگی")
    email = forms.EmailField(required=True,label="ایمیل*")
    username = forms.CharField(required=True,label="نام کاربری*")
    password = forms.CharField(required=True,label="رمز عبور*")
    confirm_password = forms.CharField(required=True,label="تکرار رمز عبور*")
    gender = forms.ChoiceField(label='جنسیت*',widget=forms.Select(attrs={'class': 'form-control'}),choices=GENDER)
    pic1 = forms.FileField(required=False)

    class Meta:
        model = TouristProfile
        fields = ('birthday','location',)

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
        self.fields['location'].label = "شهر"
        self.fields['birthday'].label = "تاریخ تولد"
        self.fields.keyOrder = ['email', 'username','firstname', 'lastname','password','confirm_password','gender', 'birthday', 'location']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("این نام کاربری قبلا انتخاب شده است")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("طول رمز عبور باید حداقل 6 کاراکتر باشد")
        return password

    def clean_confirm_password(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError(" عدم انطباق رمز عبورها با یکدیگر")
        return password2

    def save(self, commit=True):
        print('enter save')
        user = User.objects.create_user(password=self.cleaned_data['password'], username=self.cleaned_data['username']
                                        ,email=self.cleaned_data['email'])
        muser = UserM()
        muser.user = user
        if self.cleaned_data['firstname']:
            muser.user.first_name = self.cleaned_data['firstname']
        if self.cleaned_data['lastname']:
            muser.user.last_name = self.cleaned_data['lastname']
        if self.cleaned_data['pic1']:
            muser.picture = self.cleaned_data['pic1']
        muser.user.save()
        muser.kind = 'gardeshgar'
        muser.save()
        profile = super(TouristSignUpForm,self).save(commit=False)
        profile.user = muser
        if self.cleaned_data['birthday']:
            print('clean birthday')
            profile.birthday = self.cleaned_data['birthday']
        if self.cleaned_data['location']:
            profile.location = self.cleaned_data['location']
        profile.gender = self.cleaned_data['gender']
        profile.save()


class TourBuilderSignUpForm(forms.ModelForm):
    lastname = forms.CharField(required=True, label="*نام شرکت (مرکز ارائه)")
    email = forms.EmailField(required=True,label="*ایمیل شرکت")
    username = forms.CharField(required=True,label="*شماره ثبت")
    password = forms.CharField(required=True,label="*رمز عبور")
    confirm_password = forms.CharField(required=True,label="*تکرار رمز عبور")
    # kind = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices=KIND)
    pic1 = forms.FileField(required=False)

    class Meta:
        model = TourBuilderProfile
        fields = ('kind',)

    def __init__(self , *args , **kwargs):
        super(TourBuilderSignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control','placeholder': 'یک ایمیل یکتا و معتبر وارد کنید'})
        self.fields['lastname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'نام تجاری سازمان خود را وارد نمایید'})
        self.fields['username'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'شماره رسمی ثبت شرکت خود را وارد نمایید'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبوری حداقل 6 حرفی'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبور خود را دوباره وارد نمایید'})
        self.fields['kind'].label = "*نوع خدمت اصلی سازمان"
        self.fields.keyOrder = ['email','lastname', 'username','password','confirm_password', 'kind']

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.exclude(pk=self.instance.pk).get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("این شماره ثبت قبلا در سیستم ثبت گشته است")

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError("طول رمز عبور باید حداقل 6 کاراکتر باشد")
        return password

    def clean_confirm_password(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 != password2:
            raise forms.ValidationError(" عدم انطباق رمز عبورها با یکدیگر")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(password=self.cleaned_data['password'], username=self.cleaned_data['username']
                                        ,email=self.cleaned_data['email'])
        muser = UserM()
        muser.user = user
        muser.user.last_name = self.cleaned_data['lastname']
        if self.cleaned_data['pic1']:
            muser.picture = self.cleaned_data['pic1']
        muser.user.save()
        muser.kind = 'gardeshsaz'
        muser.save()
        profile = super(TourBuilderSignUpForm,self).save(commit=False)
        profile.user = muser
        profile.kind = self.cleaned_data['kind']
        profile.save()


class TourBuilderEditForm(forms.Form):
    lastname = forms.CharField(required=False, label="نام شرکت (مرکز ارائه)")
    email = forms.EmailField(required=False, label="ایمیل شرکت")
    password = forms.CharField(required=False, label="رمز عبور")
    confirm_password = forms.CharField(required=False, label="تکرار رمز عبور")

    # class Meta:
    #     model = TourBuilderProfile
    #     fields = ('kind',)

    def __init__(self , *args , **kwargs):
        super(TourBuilderEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control','placeholder': 'ایمیل جدید خود را وارد کنید'})
        self.fields['lastname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'نام تغییر یافته سازمان را وارد کنید'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبوری حداقل 6 حرفی'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبور خود را دوباره وارد نمایید'})
        self.fields.keyOrder = ['email','lastname','password','confirm_password']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) != 0:
            if len(password) < 6:
                raise forms.ValidationError("طول رمز عبور باید حداقل 6 کاراکتر باشد")
        return password

    def clean_confirm_password(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if len(password1) != 0:
            if password1 != password2:
                raise forms.ValidationError(" عدم انطباق رمز عبورها با یکدیگر")
        return password2


class TouristEditForm(forms.ModelForm):
    firstname = forms.CharField(required=False, label="نام")
    lastname = forms.CharField(required=False, label="نام خانوادگی")
    email = forms.EmailField(required=False, label="ایمیل")
    password = forms.CharField(required=False, label="رمز عبور")
    confirm_password = forms.CharField(required=False, label="تکرار رمز عبور")

    class Meta:
        model = TouristProfile
        fields = ('birthday','location',)

    def __init__(self , *args , **kwargs):
        super(TouristEditForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = forms.EmailInput(attrs={
            'class': 'form-control','placeholder': 'ایمیل جدید خود را وارد کنید'})
        self.fields['firstname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'اسم خود را وارد کنید'})
        self.fields['lastname'].widget = forms.TextInput(attrs={
            'class': 'form-control','placeholder': 'نام خانوادگی خود را وارد کنید'})
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبوری حداقل 6 حرفی'})
        self.fields['confirm_password'].widget = forms.PasswordInput(attrs={
            'class': 'form-control','placeholder': 'رمز عبور خود را دوباره وارد نمایید'})
        self.fields['birthday'].widget = forms.DateInput(attrs={
            'class': 'form-control','placeholder': 'yyyy-mm-dd'})
        self.fields['location'].widget = forms.TextInput(attrs={
            'class': 'form-control' ,'label':'شهر','placeholder': 'نام شهر محل سکونت خود را وارد نمایید'})
        self.fields['location'].label = "شهر"
        self.fields['birthday'].label = "تاریخ تولد"
        self.fields.keyOrder = ['email','firstname', 'lastname','password','confirm_password', 'birthday', 'location']

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) != 0:
            if len(password) < 6:
                raise forms.ValidationError("طول رمز عبور باید حداقل 6 کاراکتر باشد")
        return password

    def clean_confirm_password(self):

        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if len(password1) != 0:
            if password1 != password2:
                raise forms.ValidationError(" عدم انطباق رمز عبورها با یکدیگر")
        return password2
