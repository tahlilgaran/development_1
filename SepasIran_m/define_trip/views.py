from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from user.models import TourBuilderProfile,UserM
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required()
def tarif_kind(request):
    username = ''
    u1 = request.user
    if UserM.objects.filter(user = u1):
        muser = UserM.objects.filter(user = u1)[0]
        if muser.kind == 'gardeshsaz':
            username = 'gardeshsaz'

    if request.POST.get("next","") != "":
        print(request.POST.get("optradio"))
        if request.POST.get("optradio")== '1' :
            return HttpResponseRedirect('/tourdefine/hotel/')
        elif request.POST.get("optradio")== '2':
            return HttpResponseRedirect('/tourdefine/restaurant/')
        elif request.POST.get("optradio")== '3':
            return HttpResponseRedirect('/tourdefine/airplane/')
        elif request.POST.get("optradio")== '4':
            return HttpResponseRedirect('/tourdefine/train/')

    if request.POST.get("cancel","") != "":
        return HttpResponseRedirect('/userpage/')

    return  render(request,"tarif_kind.html",{
         'username': username,
    })

@login_required()
def tour_define_2(request,id):
    gardesh = Gardesh.objects.get(id = id)
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

@login_required()
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
            return HttpResponseRedirect('/tourdefine/tour/2/'+ gardesh.id)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TourForm()

    return render(request,"tour_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

@login_required()
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
            return HttpResponseRedirect('/tourdefine/airplane/2/'+ gardesh.id)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = AirPlaneForm()

    return render(request,"airplane_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

@login_required()
def airplane_define_2(request,id):

    gardesh = Gardesh.objects.get(id = id)
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

@login_required()
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
            return HttpResponseRedirect('/tourdefine/train/2/'+gardesh.id)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = TrainForm()

    return render(request,"train_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })


@login_required()
def train_define_2(request,id):

    gardesh = Gardesh.objects.get(id = id)
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


@login_required()
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
            return HttpResponseRedirect('/tourdefine/hotel/2/'+gardesh.id)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = HotelForm()

    return render(request,"hotel_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

@login_required()
def hotel_define_2(request,id):

    gardesh = Gardesh.objects.get(id = id)
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

@login_required()
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
            return HttpResponseRedirect('/tourdefine/restaurant/2/'+gardesh.id)

    elif request.POST.get("cancel","")!= "":
        return HttpResponseRedirect('/userpage/')
    else:
        form = RestaurantForm()

    return render(request,"restaurant_define.html",{
        'username': username,
        'form': form,
        'b': builder,
    })

@login_required()
def restaurant_define_2(request,id):

    gardesh = Gardesh.objects.get(id = id)
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

@login_required()
def cancel(request,name):

    return render(request,"cancel.html",{
        'username': 'gardeshsaz',
    })