from django.shortcuts import render
from define_trip.models import *
from buy_cancel.models import *
from .forms import numberForm,peopleForm,hotelForm,tableForm
# Create your views here.

def purchaseResturant(request ,id=''):
    username=request.user.username
    table=Table.objects.get(id = id)
   # table=Table.objects.filter(restaurant = resturant).get(capacity = capacity)
    restaurant=table.restaurant
    gardesh=restaurant.gardesh
    tableform=tableForm(request.POST)
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': restaurant,
             'table': table,
             'gardesh': gardesh,
             'tableform':tableform,
             'peopleform': peopleform,

            })


def purchaseTour(request ,id=''):

    username=request.user.username
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_buyer_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
    })


def purchaseAirplane(request ,id=''):
         username=request.user.username
         airplane=AirPlane.objects.get(id = id);
        # airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         form=numberForm(request.POST)
         peopleform=peopleForm(request.POST)
         return render(request, "information_of_buyer_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
              'form':form,
             'peopleform':peopleform,
             'gardesh': gardesh,
            })

def purchaseTrain(request ,id=''):
    username=request.user.username
    train=Train.objects.get(id = id);
    gardesh = train.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_buyer_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'form':form,
             'gardesh': gardesh,
             'peopleform':peopleform,

            })

def purchaseHotel(request ,id=''):
    username=request.user.username
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    form=numberForm(request.POST)
    hotelform=hotelForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request , "information_of_buyer_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,
           'form':form,
           'hotelform':hotelform,
           'peopleform':peopleform,


        })


def reserveResturant(request ,id=''):
    username=request.user.username
    table=Table.objects.get(id = id)
   # table=Table.objects.filter(restaurant = resturant).get(capacity = capacity)
    restaurant=table.restaurant
    gardesh=restaurant.gardesh
    tableform=tableForm(request.POST)
    peopleform=peopleForm(request.POST)
    return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind': 'resturant',
             'resturant': restaurant,
             'table': table,
             'gardesh': gardesh,
             'tableform':tableform,
             'peopleform': peopleform,

            })


def reserveTour(request ,id='',number=''):

    username=request.user.username
    tour=Tour.objects.get(id = id);
    gardesh=tour.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
    })

    return render(request, "information_of_reserver_tour.html" , {
             'username':username,
             'tour':tour,
             'gardesh':gardesh,
             'form':form,
             'peopleform':peopleform,
             'isclick': True,
    })


def reserveAirplane(request ,id=''):
         username=request.user.username
         airplane=AirPlane.objects.get(id = id);
        # airplaneseat=AirplaneSeat.objects.filter(airplane = airplane).filter(full = False)[0]
         gardesh=airplane.gardesh
         form=numberForm(request.POST)
         peopleform=peopleForm(request.POST)
         return render(request, "information_of_reserver_service.html" , {
             'username':username,
             'kind':'airplane',
             'airplane':airplane,
              'form':form,
             'peopleform':peopleform,
             'gardesh': gardesh,
            })

def reserveTrain(request ,id=''):
    username=request.user.username
    train=Train.objects.get(id = id);
    gardesh = train.gardesh
    form=numberForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request, "information_of_reserver_service.html" , {
            'username':username,
             'kind':'train',
             'train':train,
             'form':form,
             'gardesh': gardesh,
             'peopleform':peopleform,

            })

def reserveHotel(request ,id=''):
    username=request.user.username
    room=Room.objects.get(id = id);
    hotel=room.hotel
    gardesh=hotel.gardesh
    form=numberForm(request.POST)
    hotelform=hotelForm(request.POST)
    peopleform=peopleForm(request.POST)

    return render(request , "information_of_reserver_service.html" , {
           'username': username,
           'kind': 'hotel',
           'room': room,
           'hotel': hotel,
           'gardesh': gardesh,
           'form':form,
           'hotelform':hotelform,
           'peopleform':peopleform,


        })


def statusReserve(request,kind='', id=''):


    username = request.user.username
    number = request.POST.get("number")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    melli_num =request.POST.get("melli_number")
    tour = Tour.objects.get(id = id)
    gardesh = tour.gardesh

    #tour.capacity = tour.capacity - int(number)
    #tour.entire_capacity= tour.entire_capacity-int(number)
    #tour.save()
    for i in int(number):

        userm=request.user.userm
        gardeshgar=TouristProfile.objects.get(user =userm)
        wantedtrip= Wanted_Trip.objects.create(gardeshgar=gardeshgar , status='reserve',
                                               first_name = first_name,last_name= last_name,
                                               meli_code = melli_num,
                                               peygiry_code = 'tour'+'-'+str(tour.id)+'-'+request.user.username)
        wantedtour = Wanted_Tour.objects.create(gardesh = tour,info=wantedtrip);


    return render( request , "reserve_status.html",{
                'username':username,
                'number': number,
                'kind': kind,
                'gardesh': gardesh,
                'tour': tour,
    })



