from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from user.models import TourBuilderProfile,UserM
# Create your views here.
def tarif_kind(request,username =''):

    if request.POST.get("next","") != "":
        print("next")
        tour = request.POST.getlist("optradio")
        if tour:
            print("aval")
        if 1 in tour:
            print("write")
            return HttpResponseRedirect("/home/")

    return  render(request,"tarif_kind.html",{
         'username': username,
    })

def tour_define_2(request,):
    if name == 'badabsoort':
        name = 'باداب سورت'
    gardesh = Gardesh.objects.get(name = name)
    tour = Tour.objects.get(gardesh = gardesh)
    bazdid = Bazdid.objects.filter(tour = tour)
    if request.POST.get("return","") != "":
        tour.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/tour/')
    if request.POST.get("cancel","") != "":
        tour.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "tour_define_2.html",{
        'gardesh': gardesh,
        'tour': tour,
        'bazdids': bazdid,
        'username':"gardeshsaz",
    })


def tour_define(request):
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = TourForm(request.POST)
        d = request.POST['company']
        print(d)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'T'
            a = Agreement()
            a.kind ='tr-g'
            a.percent = '10'
            a.save()
            gardesh.agreement = a
            gardesh.degree = 'g'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if form.cleaned_data['other_explain']:
                gardesh.other_explain = request.POST.get(['other_explain'])
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            t = TransferDevice()
            t.name = request.POST.get(['company'])
            print(t.name)
            t.degree = "G"
            t.kind = "A"
            f.transfer_device = t
            l = Location()
            l.name = request.POST.get(['hotel'])
            l.kind = 'H'
            l.degree = 'G'
            l.save()
            f.stay_location = l
            f.save()
            return HttpResponseRedirect('/tourdefine/tour/2/'+gardesh.name)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TourForm()

    return render(request,"tour_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })


def airplane_define(request):
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = AirPlaneForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'A'
            gardesh.degree = 'g'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if form.cleaned_data['other_explain']:
                gardesh.other_explain = request.POST.get(['other_explain'])
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            f.save()
            return HttpResponseRedirect('/tourdefine/airplane/2/'+gardesh.name)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = AirPlaneForm()

    return render(request,"airplane_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })


def airplane_define_2(request,name):

    gardesh = Gardesh.objects.get(name = name)
    airplane = AirPlane.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        airplane.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/airplane/')
    if request.POST.get("cancel","") != "":
        airplane.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "airplane_define_2.html",{
        'gardesh': gardesh,
        'airplane': airplane,
        'username':"gardeshsaz",
    })


def train_define(request):
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)


    if request.POST.get("save","") != "":
        form = TrainForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = form.cleaned_data['name']
            gardesh.builder = builder
            gardesh.kind = 'TR'
            gardesh.degree = 'g'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if form.cleaned_data['other_explain']:
                gardesh.other_explain = request.POST.get(['other_explain'])
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            f.save()
            return HttpResponseRedirect('/tourdefine/train/2/'+gardesh.name)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TrainForm()

    return render(request,"train_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

def train_define_2(request,name):

    gardesh = Gardesh.objects.get(name = name)
    train = Train.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        train.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/train/')
    if request.POST.get("cancel","") != "":
        train.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "train_define_2.html",{
        'gardesh': gardesh,
        'train': train,
        'username':"gardeshsaz",
    })

def hotel_define(request):
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","") != "":
        form = HotelForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = builder.user.user.last_name
            gardesh.builder = builder
            gardesh.kind = 'H'
            gardesh.degree = 's'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if form.cleaned_data['other_explain']:
                gardesh.other_explain = request.POST.get(['other_explain'])
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            f.save()
            return HttpResponseRedirect('/tourdefine/hotel/2/'+gardesh.name)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = HotelForm()

    return render(request,"hotel_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

def hotel_define_2(request,name):

    gardesh = Gardesh.objects.get(name = name)
    hotel = Hotel.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        hotel.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/hotel/')
    if request.POST.get("cancel","") != "":
        hotel.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "hotel_define_2.html",{
        'gardesh': gardesh,
        'hotel': hotel,
        'username':"gardeshsaz",
    })


def restaurant_define(request):
    username = ''
    builder = ''
    u1 = request.user
    if u1:
        if UserM.objects.filter(user = u1):
            muser = UserM.objects.filter(user = u1)[0]
            if muser.kind == 'gardeshsaz':
                username = 'gardeshsaz'
                builder = TourBuilderProfile.objects.get(user = muser)

    if request.POST.get("save","") != "":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            print('valid')
            f = form.save(commit=False)
            gardesh = Gardesh()
            gardesh.name = builder.user.user.last_name
            gardesh.builder = builder
            gardesh.kind = 'R'
            gardesh.degree = 'b'
            if form.cleaned_data['free']:
                gardesh.free = form.cleaned_data['free']
            if form.cleaned_data['max_cancel_time']:
                gardesh.max_cancel_time = form.cleaned_data['max_cancel_time']
            if form.cleaned_data['other_explain']:
                gardesh.other_explain = request.POST.get(['other_explain'])
                print(gardesh.other_explain)
            gardesh.save()
            f.gardesh = gardesh
            f.save()
            return HttpResponseRedirect('/tourdefine/restaurant/2/'+gardesh.name)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = RestaurantForm()

    return render(request,"restaurant_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })


def restaurant_define_2(request,name):

    gardesh = Gardesh.objects.get(name = name)
    restaurant = Restaurant.objects.get(gardesh = gardesh)
    if request.POST.get("return","") != "":
        restaurant.delete()
        gardesh.delete()
        return HttpResponseRedirect('/tourdefine/restaurant/')
    if request.POST.get("cancel","") != "":
        restaurant.delete()
        gardesh.delete()
        return HttpResponseRedirect('/userpage/')
    if request.POST.get("save","") != "":
        return HttpResponseRedirect('/userpage/')

    return render(request, "restaurant_define_2.html",{
        'gardesh': gardesh,
        'restaurant': restaurant,
        'username':"gardeshsaz",
    })

def cancel(request,username):

    return render(request,"cancel.html",{
        'username': username,
    })