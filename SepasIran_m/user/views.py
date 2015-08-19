from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import TouristSignUpForm ,TourBuilderSignUpForm,TourBuilderEditForm,TouristEditForm
from .models import TouristProfile,TourBuilderProfile,UserM
import datetime
# Create your views here.


def signin(request):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ورود به سایت'
    if request.POST.get("signup","") != "":
        return HttpResponseRedirect('/signup/')
    if request.POST.get("forget","") != "":
        return HttpResponseRedirect('/forgetpassword/')
    wrong = 'false'
    usernamep = ''
    if request.POST.get("login","")!= "":
        username = request.POST.get("username", "")
        password = request.POST.get("pwd", "")
        user = authenticate(username=username,password=password)

        if user:
            u = User.objects.get(username = username)
            userm = UserM.objects.get(user = u)
            if userm.kind == 'gardeshgar':
                if u.userm.tprofile.has_payed:
                    login(request, user)
                    return HttpResponseRedirect('/userpage/')
                else:
                    wrong = 'notpayed'
                    usernamep = username
            else :
                login(request, user)
                if username == 'admin':
                    return HttpResponseRedirect('/manager/Dashboard/')
                return HttpResponseRedirect('/userpage/')

        else:
            wrong = "wrongpass"

    return render(request, "login.html",{
        'username': "",
        'wrong':wrong,
        'usernamep': usernamep,
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def forget_password(request):
    date = datetime.datetime.now()
    sended = 1
    user2 = request.user
    position = 'فراموشی رمز عبور'
    if request.POST.get("cancel","") != "":
        return HttpResponseRedirect('/signIn/')
    if request.method == 'POST':
        u = User.objects.filter(email=request.POST.get("email", ""))

        if not u:
            sended=0
        else:
            sended = 2
            u[0].set_password('123456')
            u[0].save()
    return render(request, "forget.html", {
            'has_send': sended,
            'username': "",
            'user2':user2,
            'position': position,
            'tarikh':date,
            })


def signup(request):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام کاربران'
    if request.POST.get("next","") != "":
        print(request.POST.get("optradio"))
        if request.POST.get("optradio")== '1' :
            return HttpResponseRedirect('/signup/tourist/')
        else:
            return HttpResponseRedirect('/signup/tourBuilder/')

    if request.POST.get("cancel","") != "":
        return HttpResponseRedirect('/signIn/')
    return render(request, "signup.html",{
        'username': "",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def tourist_signup(request):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام گردشگران> ورود اطلاعات'
    if request.POST.get("save","") != "":
        form = TouristSignUpForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            us = User.objects.get(username = username)
            usm = UserM.objects.get(user = us)
            if form.cleaned_data['pic1']:
                usm.picture = form.cleaned_data['pic1']
                usm.save()
            return HttpResponseRedirect('/signup/tourist/2/'+username)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/signIn/')
    else:
        form = TouristSignUpForm()

    return render(request, "signup_tourist.html",{
        'username':'',
        'form': form,
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def tourist_signup_2(request,username):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام گردشگران> ورود اطلاعات> تایید اطلاعات'
    user = User.objects.get(username = username)
    userm = UserM.objects.get(user = user)
    profile = TouristProfile.objects.get(user = userm)

    if request.POST.get("confirm","") != "":
        return HttpResponseRedirect('/signup/tourist/3/'+username)
    if request.POST.get("return","") != "":
        profile.delete()
        userm.delete()
        user.delete()
        return HttpResponseRedirect('/signup/tourist/')
    if request.POST.get("cancel","") != "":
        profile.delete()
        userm.delete()
        user.delete()
        return HttpResponseRedirect('/signIn/')

    return render(request,"signup_tourist2.html",{
        'user': user,
        'profile': profile,
        'username': "",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })

def tourist_signup_3(request,username):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام گردشگران> ورود اطلاعات> تایید اطلاعات> پرداخت هزینه عضویت'
    user = User.objects.get(username = username)
    userm = UserM.objects.get(user = user)
    profile = TouristProfile.objects.get(user = userm)

    if request.POST.get("confirm","") != "":
        return HttpResponseRedirect('/payment/'+username)

    if request.POST.get("cancel","") != "":
        profile.delete()
        userm.delete()
        user.delete()
        return HttpResponseRedirect('/signIn/')

    return render(request,"signup_tourist3.html",{
        'user': user,
        'username': "",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/signIn/')


def servant_signup(request):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام گردش سازان> ورود اطلاعات'
    if request.POST.get("save","") != "":
        form = TourBuilderSignUpForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            # user = User.objects.create_user(password=form.cleaned_data['password'], username=form.cleaned_data['username']
            #                             ,email=form.cleaned_data['email'])
            # muser = UserM()
            # muser.user = user
            # muser.user.last_name = form.cleaned_data['lastname']
            # if form.cleaned_data['pic1']:
            #     muser.picture = form.cleaned_data['pic1']
            # muser.user.save()
            # muser.kind = 'gardeshsaz'
            # muser.save()
            # profile = TourBuilderProfile()
            # profile.user = muser
            # profile.kind = form.cleaned_data['kind']
            # profile.save()
            username = form.cleaned_data['username']
            return HttpResponseRedirect('/signup/tourBuilder/2/'+username)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/signIn/')
    else:
        form = TourBuilderSignUpForm()

    return render(request, "signup_tourBuilder.html",{
        'username': "",
        'form': form,
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def servant_signup_2(request,username):
    date = datetime.datetime.now()
    user2 = request.user
    position = 'ثبت نام گردش سازان> ورود اطلاعات> تایید اطلاعات و قرارداد'
    user = User.objects.get(username = username)
    userm = UserM.objects.get(user = user)
    profile = TourBuilderProfile.objects.get(user = userm)

    if request.POST.get("return","") != "":
        profile.delete()
        userm.delete()
        user.delete()
        return HttpResponseRedirect('/signup/tourBuilder/')
    if request.POST.get("cancel","") != "":
        profile.delete()
        userm.delete()
        user.delete()
        return HttpResponseRedirect('/signIn/')
    if request.POST.get("save","") != "":
        # userl = authenticate(username=username,password=password)
        # if user:
        #     login(request, userl)
        return HttpResponseRedirect('/signIn/')

    return render(request, "signup_tourBuilder2.html",{
        'user': user,
        'profile': profile,
        'username':"",
        'user2': user2,
        'position': position,
        'tarikh':date,
    })


def edit_tourist(request,username):
    date = datetime.datetime.now()
    position = 'تغییر اطلاعات گردشگر'
    user = request.user
    user2 = User.objects.get(username = username)
    if user != user2:
        return HttpResponseRedirect('/profile/tourist/'+username)
    muser = UserM.objects.get(user = user)
    profile = TouristProfile.objects.get(user = muser)
    if request.POST.get("edit","") != "":
        form = TouristEditForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password:
                user.set_password(password)
            email = form.cleaned_data['email']
            if email:
                user.email = email
            lastname = form.cleaned_data['lastname']
            if lastname:
                user.last_name = lastname
            firstname = form.cleaned_data['firstname']
            if firstname:
                user.first_name = firstname
            user.save()
            birthday = form.cleaned_data['birthday']
            if birthday:
                profile.birthday = birthday
            location = form.cleaned_data['location']
            if location:
                profile.location = location
            muser.save()
            profile.save()
            u = authenticate(username = username,password = password)
            if u:
                login(request,u)
            return HttpResponseRedirect('/profile/tourist/'+username)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/profile/tourist/'+username)
    else:
        form = TouristEditForm()

    return render(request, "edit_tourist.html",{
        'username':"gardeshgar",
        'form': form,
        'user2': user,
        'position': position,
        'tarikh':date,
    })


def edit_tourbuilder(request,username):
    date = datetime.datetime.now()
    position = 'تغییر اطلاعات گردش ساز'
    user = request.user
    user2 = User.objects.get(username = username)
    if user != user2:
        return HttpResponseRedirect('/profile/tourbuilder/'+username)
    muser = UserM.objects.get(user = user)
    profile = TourBuilderProfile.objects.get(user = muser)
    if request.POST.get("edit","") != "":
        form = TourBuilderEditForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            if password:
                user.set_password(password)
            email = form.cleaned_data['email']
            if email:
                user.email = email
            lastname = form.cleaned_data['lastname']
            if lastname:
                user.last_name = lastname
            user.save()
            muser.save()
            profile.save()
            u = authenticate(username = username,password = password)
            if u:
                login(request,u)
            return HttpResponseRedirect('/profile/tourbuilder/'+username)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/profile/tourbuilder/'+username)
    else:
        form = TourBuilderEditForm()

    return render(request, "edit_tourbuilder.html",{
        'username':"gardeshsaz",
        'form': form,
        'user2': user,
        'position': position,
        'tarikh':date,
    })


def tourist_profile(request,username):
    date = datetime.datetime.now()
    position = 'مشاهده اطلاعات گردشگر'

    if User.objects.filter(username = username):
        user = User.objects.filter(username = username)[0]
        user2 = request.user
        userm = UserM.objects.filter(user = user2)[0]
        if user != user2 and userm.kind != 'manager':
            return HttpResponseRedirect('/signIn/')
        muser = UserM.objects.get(user = user)
        profile = TouristProfile.objects.get(user = muser)
    else:
        return HttpResponse("<html><head></head><body>there is no user with this username</body></html>")

    if request.POST.get("edit","") != "":
        return HttpResponseRedirect('/edit/tourist/'+username)
    if request.POST.get("cancel","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "tourist_profile.html",{
        'username': "gardeshgar",
        'profile': profile,
        'user': user,
        'user2': user2,
        'position': position,
        'tarikh':date,
    })

def tourbuilder_profile(request,username):
    date = datetime.datetime.now()
    position = 'مشاهده اطلاعات گردش ساز'
    user2 = request.user
    me= False

    if User.objects.filter(username = username):
        user = User.objects.filter(username = username)[0]
        muser = UserM.objects.get(user = user)
        profile = TourBuilderProfile.objects.get(user = muser)

    else:
        return HttpResponse("<html><head></head><body>there is no user with this username</body></html>")
    if user == user2:
        me = True
    if request.POST.get("edit","") != "":
        return HttpResponseRedirect('/edit/tourbuilder/'+username)
    if request.POST.get("cancel","") != "":
        if me:
            return HttpResponseRedirect('/userpage/')
        else:
            return HttpResponseRedirect('/home/')
    return render(request, "tourbuilder_profile.html",{
        'username': "gardeshsaz",
        'profile': profile,
        'user': user,
        'me': me,
        'user2': user2,
        'position': position,
        'tarikh':date,
    })

def sepas(request):
    user2 = request.user
    date = datetime.datetime.now()
    return render(request,'sepas.html',{
        'tarikh':date,
        'user2': user2,

    })

def hadaf(request):
    user2 = request.user
    date = datetime.datetime.now()
    return render(request,'hadaf.html',{
        'tarikh':date,
        'user2': user2,
    })

def tahlilgaran(request):
    user2 = request.user
    date = datetime.datetime.now()
    return render(request,'tahlilgaran.html',{
        'tarikh':date,
        'user2': user2,

    })

def rotbe(request):
    user2 = request.user
    date = datetime.datetime.now()
    return render(request,'rotbe.html',{
        'tarikh':date,
        'user2': user2,
    })