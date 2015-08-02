from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import TouristSignUpForm ,TourBuilderSignUpForm,TourBuilderEditForm,TouristEditForm
from .models import TouristProfile,TourBuilderProfile,UserM
# Create your views here.


def signin(request):

    if request.POST.get("signup","") != "":
        return HttpResponseRedirect('/signup/')
    if request.POST.get("forget","") != "":
        return HttpResponseRedirect('/forgetpassword/')
    wrong = 'false'
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
    })


def forget_password(request):
    sended = 1

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
            })


def signup(request):
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
    })


def tourist_signup(request):

    if request.POST.get("save","") != "":
        form = TouristSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            userl = authenticate(username=username,password=password)
            if userl:
                login(request, userl)
                return HttpResponseRedirect('/signup/tourist/2/'+username)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/signIn/')
    else:
        form = TouristSignUpForm()

    return render(request, "signup_tourist.html",{
        'username':'',
        'form': form,
    })


def tourist_signup_2(request,username):
    user = User.objects.get(username = username)
    userm = UserM.objects.get(user = user)
    profile = TouristProfile.objects.get(user = userm)

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
    })


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/signIn/')


def servant_signup(request):

    if request.POST.get("save","") != "":
        form = TourBuilderSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('/signup/tourBuilder/2/'+username+'/'+password)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/signIn/')
    else:
        form = TourBuilderSignUpForm()

    return render(request, "signup_tourBuilder.html",{
        'username': "",
        'form': form,
    })


def servant_signup_2(request,username,password):
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
        userl = authenticate(username=username,password=password)
        if user:
            login(request, userl)
            return HttpResponseRedirect('/userpage/')

    return render(request, "signup_tourBuilder2.html",{
        'user': user,
        'profile': profile,
        'username':"",
    })


def edit_tourist(request,username):
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
    })


def edit_tourbuilder(request,username):
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
            kind = form.cleaned_data['kind']
            if kind:
                profile.kind = kind
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
    })


def tourist_profile(request,username):

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
    })

def tourbuilder_profile(request,username):
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
    })