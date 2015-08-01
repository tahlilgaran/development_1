from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .forms import TouristSignUpForm ,TourBuilderSignUpForm
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
                return HttpResponseRedirect('/userpage/')
            if username == 'admin':
                return HttpResponseRedirect('/manager/Dashboard/')

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

    return render(request, "signup.html",{
        # 'username':username,
    })


def tourist_signup(request):

    if request.POST.get("save","") != "":
        form = TouristSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            return HttpResponseRedirect('/signup/tourist/2/'+username)

            # password = form.cleaned_data['password']
            # user = authenticate(username=username,password=password)
            # if user:
            #     login(request, user)
            #     return HttpResponseRedirect('/userpage/')

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

    return render(request, "edit_tourist.html",{
        'username':username,
    })


def edit_tourbuilder(request,username):
    print('edit')
    return render(request, "edit_tourbuilder.html",{
        'username':username,
    })


def tourist_profile(request,username):

    return render(request, "tourist_profile.html",{
        'username':username,
    })
def tourbuilder_profile(request,username):
    print('profile.')
    return render(request, "tourbuilder_profile.html",{
        'username':username,
    })